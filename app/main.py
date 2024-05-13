import logging
import uvicorn

from sqlalchemy.orm import Session

from fastapi import FastAPI, Request, Depends
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles


from app.config import settings
from app.dependencies import get_db_session

from app.db.models import IPStats
from app.db.crud import get_ips_from_stats, insert_ip_to_stats


logging.basicConfig(level=logging.DEBUG)


app = FastAPI()
app.mount("/static", StaticFiles(directory="app/static"), name="static")

index_html = """
<!DOCTYPE html>
<html>
    <head>
        <meta charset="UTF-8">
        <title>哎呀 又中一计</title>
        <style>
            body {
                width: 35em;
                margin: 0 auto;
            }
            footer {
                width: 100%;
                position: fixed;
                bottom: 0;
                left: 0;
                background-color: #f5f5f5;
                color: #6c757d;
                text-align: center;
                padding: 10px 0;
            }
            footer p {
                margin: 0;
                font-family: Arial, sans-serif;
            }
        </style>
    </head>
    <body>
        <h1>嘻嘻 ... ... 他真的信了，他全信了 ~!</h1>
        <img src="/static/imgs/index.png" height=600px/>
        <p>累计被骗人数： total_num</p>
        
        <footer>
            <p><small>北京漫展坐忘道群友六二六</small></p>
        </footer>
    </body>
</html>

"""


@app.get("/", response_class=HTMLResponse)
async def index(request: Request, db: Session = Depends(get_db_session)):
    global index_html

    client_host = request.client.host
    ips = get_ips_from_stats(db=db)

    if client_host in ips:
        return index_html.replace("total_num", str(len(ips)))
    else:
        ip_stat = IPStats(ip=client_host)
        insert_ip_to_stats(db, ip_stat)
        return index_html.replace("total_num", str(len(ips) + 1))


if __name__ == "__main__":
    uvicorn.run(app, host=settings.api_host, port=settings.api_port)
