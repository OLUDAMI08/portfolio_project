from sqlalchemy import create_engine, text


engine = create_engine("mysql+pymysql://root:@localhost:3306/empowerCo")


def jobs_load_from_db():
    with engine.connect() as conn:
        query = text('SELECT * FROM jobs')
        results = conn.execute(query)

        jobs = []
        for row in results.all():
            row_dict = row._asdict()
            jobs.append(row_dict)
        return (jobs)


def load_job_from_db(id):
    with engine.connect() as conn:
        query = text('SELECT * FROM jobs WHERE id = :val')
        results = conn.execute(query.params(val=id))

        rows = results.all()

        if len(rows) == 0:
            return None
        else:
            return rows[0]._asdict()


# def add_application_to_db(job_id, data):
#     with engine.connect() as conn:
#         query = text('INSERT INTO application(job_id, full_name, email, linkedin_url, education, resume_url) VALUES(:job_id, :full_name, :email, :linkedin_url, :education, :resume_url)')
#         conn.execute(query, job_id=job_id, **data)


# def add_application_to_db(job_id, data):
#     with engine.connect() as conn:
#         query = text("INSERT INTO application(job_id, full_name, email, linkedin_url, education, resume_url) VALUES(:id, :full_name, :email, :linkedin_url, :education, :resume_url)")
#         conn.execute(query,
#                      job_id=job_id,
#                      full_name=data['full_name'],
#                      email=data['email'],
#                      linkedin_url=data['linkedin_url'],
#                      education=data['education'],
#                      resume_url=data['resume_url']
#                      )

def add_application_to_db(job_id, data):
    with engine.connect() as conn:
        query = text("INSERT INTO application (job_id, full_name, email, linkedin_url, education, resume_url) VALUES(:job_id, :full_name, :email, :linkedin_url, :education, :resume_url)")
        params = {
            'job_id': job_id,
            'full_name': data['full_name'],
            'email': data['email'],
            'linkedin_url': data['linkedin_url'],
            'education': data['education'],
            'resume_url': data['resume_url']
        }
        conn.execute(query, params)
        conn.commit()
