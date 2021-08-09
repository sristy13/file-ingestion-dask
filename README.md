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
#### Total 500000 records in target table. Sample 10 rows
| name        | sku           | description  |
| ------------- |:-------------:| -----:|
| John Bailey |	course-there |	Whatever realize recently. Mind start next task. Organization experience present simple describe cover while garden.Moment professional beyond open. That open realize minute special.|
Mario Green |	hotel-trip-human |	Especially model candidate human than. Help watch carry ask any good. Site blood season in various easy order.Send often open whom avoid pull.|
Patricia Davis |	wide-movie-despite |	Magazine development food talk election. Congress television near difference hospital behind a. Government she arm they area low.|
Elizabeth Poole |	each-officer |	Student town artist another exactly. Rise majority before today tonight establish operation. |
Tina Morris |	service-reduce |	Pretty pass million cup spring voice discuss. Week admit discover necessary above use cost. Run those brother bill current.
William Walker |	reflect-term-memory |	Light discussion clearly news challenge third drive. City perhaps very. House career range media. Section push allow man society final exactly. |
Bryan Kelly |	real-forget |	Source glass blood them. Tend bring task. Sound yeah feel son behind.Low between play financial discover treatment somebody. |
Craig Tucker |	information-hour |	Break American down wife draw. Cold start operation how appear lot. |
Amber Olson |	choose-though |	Economic where result wall. Defense employee large. Clear his way fish.Bed standard or its. Challenge simply under subject citizen pass course. College church investment everything key.|
Cynthia Cain |	finish-agreement |	Relate choice floor. Since travel bring say past no air. Particular great issue build. Key bank chance policy recent call almost.      | 

#### Total 444048 records in aggregated table. Sample 10 rows
| name | number_of_products|
| ------------- |:-------------:|
|Luis Swanson Jr. |	1 |
Tiffany Choi |	1 |
Matthew Hunt |	8 |
William Carey |	3 |
Evan Lin |	1 |
Erin Young |	6 |
Antonio Woods |	1 |
Luis Hodges |	1 |
Emily Weber |	2 |
Norman Ryan |	1 |
## Incompleted tasks
None
## Further improvements
1. Can explore Spark for parallel processing and compare current performance with Spark jobs.
2. Can check Postgres performance with other databases and choose the best database according to performance.
3. Can schedule the data ingestion job for daily run.



  
