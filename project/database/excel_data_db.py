import datetime

import sqlalchemy as data

from .db import metadata

excel_data = data.Table(
    "excel_data",
    metadata,
    data.Column("id", data.Integer, primary_key=True, autoincrement=True, unique=True),
    data.Column("date", data.DateTime, default=datetime.datetime.utcnow()),
    data.Column("company", data.String),
    data.Column("plan_fact", data.String),
    data.Column("plan_forecast", data.String),
    data.Column("identification", data.String),
    data.Column("count", data.Integer)
)
