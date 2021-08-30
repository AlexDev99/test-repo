from .db import metadata, engine
from .excel_data_db import excel_data
metadata.create_all(bind=engine)
