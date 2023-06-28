from sqlalchemy import create_engine, text


engine = create_engine("mysql+pymysql://root:@localhost/empowerCo")


def jobs_load_from_db():
    with engine.connect() as conn:
      query = text('SELECT * FROM jobs')
      results = conn.execute(query)

      jobs = []
      for row in results.all():
        row_dict = row._asdict()
        jobs.append(row_dict)
      return(jobs)
    
def load_job_from_db(id):
   with engine.connect() as conn:
      query = text('SELECT * FROM jobs WHERE id = :val')
      results = conn.execute(query.params(val=id))

      rows = results.all()

      if len(rows) == 0:
         return None
      else:
         return rows[0]

   


   
    
    
