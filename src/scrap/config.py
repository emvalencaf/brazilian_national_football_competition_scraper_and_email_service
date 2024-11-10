from os import getenv
from typing import Tuple
from scrap.schemas import CompetitionID
from pydantic_settings import BaseSettings
from dotenv import load_dotenv

load_dotenv()

class ScrapSettings(BaseSettings):
    FROM_EMAIL_ADDRESS: str = str(getenv('FROM_EMAIL_ADDRESS', ''))
    FROM_EMAIL_PASSWORD: str = str(getenv('FROM_EMAIL_PASSWORD', ''))
    
    BASE_URL: str = 'https://www.academiadasapostasbrasil.com/stats/competition/brasil/26'
    
    ID_COMPETITIONS: Tuple[CompetitionID, ...] = (
        CompetitionID(id='139', season=1998),
        CompetitionID(id='577', season=1999),
        CompetitionID(id='578', season=2000),
        CompetitionID(id='579', season=2001),
        CompetitionID(id='580', season=2002),
        CompetitionID(id='581', season=2003),
        CompetitionID(id='735', season=2004),
        CompetitionID(id='947', season=2005),
        CompetitionID(id='1495', season=2006),
        CompetitionID(id='1965', season=2007),
        CompetitionID(id='2598', season=2008),
        CompetitionID(id='3220', season=2009),
        CompetitionID(id='4996', season=2010),
        CompetitionID(id='5830', season=2011),
        CompetitionID(id='6826', season=2012),
        CompetitionID(id='7971', season=2013),
        CompetitionID(id='9097', season=2014),
        CompetitionID(id='11185', season=2015),
        CompetitionID(id='12284', season=2016),
        CompetitionID(id='13464', season=2017),
        CompetitionID(id='15366', season=2018),
        CompetitionID(id='16888', season=2019),
        CompetitionID(id='18427', season=2020),
        CompetitionID(id='91BVQJ6p7Qwa6', season=2021),
        CompetitionID(id='gEyAmA0DWZ2po', season=2022),
        CompetitionID(id='NR2zmkLnBQ08o', season=2023),
        CompetitionID(id='MPvoQox4VYlOy', season=2024),
    )
    
scrap_settings = ScrapSettings()