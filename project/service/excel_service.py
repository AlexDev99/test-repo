from project.model.excel_model import ExcelModel
from ..database.db import database
from ..database.excel_data_db import excel_data


async def create_post(post: ExcelModel):
    query = (
        excel_data.insert()
            .values(
            company=post.name_company,
            date=post.fact.count.get(),
            plan_fact=post.fact.count.values(),
            plan_forecast=post.fact.count.values()
        )
            .returning(
            excel_data.c.id,
            excel_data.c.company,
            excel_data.c.plan_fact,
            excel_data.c.plan_forecast,
        )
    )
    await database.fetch_one(query)
