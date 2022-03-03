SHELL = /bin/bash
m_env:
	source ./venv/bin/activate

m_init:
	r8 sql init --origin http://localhost:8000
	r8 sql file config.sql

m_run:
	r8 run

init:
	make m_env
	make m_init

run:
	make m_env
	make m_run	
