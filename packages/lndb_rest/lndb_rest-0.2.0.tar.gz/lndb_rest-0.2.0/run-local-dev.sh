export LAMIN_SKIP_MIGRATION=true
export LAMIN_ENV="dev"
export email="frederic.enard@gmail.com"
export password="WutHYQ2tRDvj7OqYQTiJNU6Q3M1lE7SGHOF64tYa"
export storage="instance-test-1-storage"
export schema="bionty,wetlab,bfx"
export db="postgresql://postgres:rbus9LA8GR!s5jC@db.vqoghtjntbkjpnrcskla.supabase.co:5432/postgres"

lndb login $email --password $password
lndb init --storage $storage --schema $schema --db $db

python3 ./lndb_rest/main.py
