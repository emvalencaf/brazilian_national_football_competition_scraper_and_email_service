from io import BytesIO
from fastapi import APIRouter, HTTPException

from scrap.schemas import RequestEmail
from scrap.config import scrap_settings
from scrap.services import get_all_competition_dataframe, send_email_with_attachment

router = APIRouter(tags=['scrap', 'email'])



@router.post('/send_email', description="Send a email with brazilian national competition attach")
async def send_email(request: RequestEmail):
    try:
        # Get ids from the request season
        ids = [competition.id for competition in scrap_settings.ID_COMPETITIONS if competition.season in request.seasons]

        # Get the dataframe asynchronously
        df = await get_all_competition_dataframe(ids=ids)

        # Create the Excel file in memory
        excel_file = BytesIO()
        df.to_excel(excel_file, index=False, engine='openpyxl')
        excel_file.seek(0)

        # Send the email with the attached Excel file
        send_email_with_attachment(request.email, excel_file)

        return {"message": "Excel file was successfully sent!"}
    
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail=f"An error occurred: {str(e)}")