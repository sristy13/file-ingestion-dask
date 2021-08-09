# postman-assignment
Large file ingestion from CSV to Postgres database using parallel processing

## Steps to run
### Setup target database(Postgres) in Docker
```
docker pull postgres
docker run --name pg-docker -e POSTGRES_PASSWORD=docker -d -p 5432:5432 postgres
```

### Clone github repository
```
git clone https://github.com/sristy13/postman-assignment.git
```
### Required changes
```
Change host name to database IP in REPO_URL present in env file
```
### Build application Docker image
```
docker build -t postman-assignment .
```
### Run Docker image
```
docker run --name ingestion-assignment postman-assignment
```

## Schema details
Target table name - products<br />
DDL Query:

``` 
CREATE TABLE public.products (
	name varchar(250) NULL,
	sku varchar(250) NULL,
	description text NULL
); 
```
Aggregated data in table - aggregared_table<br />
DDL Query:
```
CREATE TABLE public.aggregated_table (
	name varchar(250) NULL,
	number_of_products int4 NULL
);
```
## Completed tasks
1. Created multiple classes, objects and methods to follow best practices of OOP.
2. Used Dask dataframe to achieve parallel processing and successfully completed ingestion job within a minute.
3. To support updation of existing records, Created a temp table of incoming data and delete records from target table present in temp table and then loaded incoming data to target.
4. Ingested entire records to single target table i.e. products.
5. Created an aggregated table which has two columns "name" and "number_of_products" to store aggregated data.

## Further improvements
1. Can explore Spark for parallel processing and compare current performance with Spark jobs.
2. Can check Postgres performance with other databases and choose the best database according to performance.



  
