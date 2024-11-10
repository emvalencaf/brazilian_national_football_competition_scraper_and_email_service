import asyncio
from typing import List, Tuple

from bs4 import BeautifulSoup, NavigableString, Tag
import aiohttp
import pandas as pd
import re
from io import BytesIO
import smtplib
from email.message import EmailMessage
from scrap.utils import format_date
from scrap.config import scrap_settings

async def scrap(urls: List[str]) -> List[BeautifulSoup]:
    async with aiohttp.ClientSession() as session:
        tasks = [session.get(url) for url in urls]
        responses = await asyncio.gather(*tasks)
        
        soups = [BeautifulSoup(await response.text(), 'html.parser') for response in responses]
        return soups

def extract_data_table(table: Tag | NavigableString, 
                       competition: str, 
                       season: int) -> Tuple[List[str], List[str], List[str], List[str], List[str], List[str], List[str], List[int]]:
    dates = []
    times = []
    hosts = []
    visitors = []
    scores = []
    rounds = []
    competitions = []
    seasons = []

    for line in table.find_all('tr', id=True):
        columns = line.find_all('td')
        if len(columns) >= 6:
            datetime_str = columns[1].get_text(strip=True)
            
            date_match = re.search(r"(\d{2}\.\w{3}\.\d{4})", datetime_str)
            time_match = re.search(r"(\d{2}:\d{2})", datetime_str)
            
            date = format_date(date_match.group(0)) if date_match else None
            time = time_match.group(0) if time_match else None
            
            host = columns[2].get_text(strip=True)
            score = columns[3].get_text(strip=True)
            visitor = columns[4].get_text(strip=True)
            round = columns[5].get_text(strip=True)

            dates.append(date)
            times.append(time)
            hosts.append(host)
            scores.append(score)
            visitors.append(visitor)
            rounds.append(round)
            competitions.append(competition)
            seasons.append(season)
    
    return dates, times, hosts, visitors, scores, rounds, competitions, seasons

def extract_table(soups: List[BeautifulSoup]) -> pd.DataFrame:
    all_dates, all_times, all_hosts, all_visitors, all_scores, all_rounds, all_competitions, all_seasons = [], [], [], [], [], [], [], []
    
    for soup in soups:
        table = soup.find('table', class_='competition-rounds competition-half-padding')
        bread_ul_lis = soup.find('div', class_='breadcrumbs').find_all('li')

        competition = bread_ul_lis[2].a['title']
        season = bread_ul_lis[3].a['title']

        if table:
            dates, times, hosts, visitors, scores, rounds, competitions, seasons = extract_data_table(table=table,
                                                                                                      competition=competition,
                                                                                                      season=season)
            all_dates.extend(dates)
            all_times.extend(times)
            all_hosts.extend(hosts)
            all_visitors.extend(visitors)
            all_scores.extend(scores)
            all_rounds.extend(rounds)
            all_competitions.extend(competitions)
            all_seasons.extend(seasons)
    
    df = pd.DataFrame({
        "Date": all_dates,
        "Time": all_times,
        "Host": all_hosts,
        "Visitor": all_visitors,
        "Score": all_scores,
        "Round": all_rounds,
        "Competition": all_competitions,
        "Season": all_seasons,
    })

    return df

async def get_competitions_data(id_competition: str) -> pd.DataFrame:
    urls = [
        f"{scrap_settings.BASE_URL}/{id_competition}/all-games",
        f"{scrap_settings.BASE_URL}/{id_competition}/all-games/page/2"
    ]
    soups = await scrap(urls=urls)
    df = extract_table(soups=soups)
    return df

async def get_all_competition_dataframe(ids: List[str]) -> pd.DataFrame:
    tasks = [get_competitions_data(id) for id in ids]
    dfs = await asyncio.gather(*tasks)
    dfs_final = pd.concat(dfs, ignore_index=True)
    return dfs_final

def send_email_with_attachment(to_email: str,
                               attachment: BytesIO):
    msg = EmailMessage()
    msg["Subject"] = "Dados das Partidas do Brasileirão Série A"
    msg["From"] = "seu_email@gmail.com"  # Substitua pelo seu e-mail
    msg["To"] = to_email
    msg.set_content("Segue em anexo o arquivo Excel com os dados do campeonato série A do Brasileirão.")

    # Anexar o arquivo Excel
    msg.add_attachment(attachment.getvalue(),
                       maintype="application",
                       subtype="octet-stream", filename="dados_competicoes.xlsx")

    # Enviar o e-mail
    with smtplib.SMTP_SSL("smtp.gmail.com",
                          465) as server:
        server.login(scrap_settings.FROM_EMAIL_ADDRESS,
                     scrap_settings.FROM_EMAIL_PASSWORD)  # Substitua pelo seu e-mail e senha
        server.send_message(msg)
        
