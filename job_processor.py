from mysite import db
from mysite.database import create_tables
from mysite.models import Job
from jobs import sitescan

def run_job():
    pass
    #query database for jobs to run
    job = Job.query.filter_by(status=-1).first()
    if job:
        print(job.function)
        run = exec(job.function+".run()")
        if run:
            print(run)
            run()
            job.status = 0
            db.commit()

    #clear job from database
    #send logs/status

if __name__ == "__main__":
    create_tables()
    job = Job(function="sitescan",
              status=-1)
    db.session.add(job)
    db.session.commit()
    run_job()
