#! /bin/bash    
source /home/ec2-user/flask_env/bin/activate

# virtualenv is now active, which means your PATH has been modified.
# Don't try to run python from /usr/bin/python, just run "python" and
# let the PATH figure out which version to run (based on what your
# virtualenv has configured).

python /home/ec2-user/cherry_app/bhav_csv_generator.py
