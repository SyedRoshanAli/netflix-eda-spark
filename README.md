#### ***Dataset for this project*** : https://www.kaggle.com/code/akshatjainds/netflix-movies-and-tv-shows





# Spark Docker Setup and Execution

This project demonstrates how to set up Apache Spark on a Docker container and perform basic operations using Python and Spark's PySpark library. Follow the steps below to replicate the setup and execution.

---

## Prerequisites

First I Ensured the following are installed on my system:
   **Java**: OpenJDK 1.8 or above
   ```bash
   java -version
   ```
   Output:
   ![6D1669AC-128A-4984-84B5-CB950D7675F4_1_201_a](https://github.com/user-attachments/assets/d3dc1c72-edff-40ba-a987-9d004cacfe8a)


   **Python**: Python 3.9 or above
   ```bash
   python3 --version
   ```
   Output:
   ![6D1669AC-128A-4984-84B5-CB950D7675F4_4_5005_c](https://github.com/user-attachments/assets/f29f2c76-ddf6-4b2a-ae00-8d9a1b8f6bc9)


---

## Setting Up Apache Spark

   **Download and Extract Spark**:  
   Placed the extracted Spark folder on my Desktop.

   **Set the SPARK_HOME environment variable**:  
      ![6D1669AC-128A-4984-84B5-CB950D7675F4_1_201_a](https://github.com/user-attachments/assets/ae263964-2b99-4ec2-8c3a-362d98fbe3c6)

   **Verify Spark Installation**:  
   I Run the following command to check if Spark is correctly installed:
   - Spark Shell (Scala):
     ```bash
     spark-shell --version
     ```
     Output:
      ![6D1669AC-128A-4984-84B5-CB950D7675F4_1_201_a](https://github.com/user-attachments/assets/d88daf35-2165-45a4-8cdc-d7b47a675599)

     
   - PySpark:
     ```bash
     pyspark
     ```
     <img width="1599" alt="Screenshot 2024-12-13 at 8 12 02 PM" src="https://github.com/user-attachments/assets/272b9391-23a8-44d0-b9f7-5f3f4b0d4f4c" />

   Run a PySpark example:
   Placed the Python script (`EDA_netflix.py`) in the Spark folder and execute:
   ```bash
   python EDA_netflix.py
   ```
   Output : "Run python file to get output"


# Pulling Docker Image for Spark

   **Runing my Python script:**
   running command **"python EDA_netflix.py"**

   Output:

   <img width="1169" alt="Screenshot 2024-12-14 at 1 19 29 AM" src="https://github.com/user-attachments/assets/396664ab-b46c-4104-9217-3ea32e553b5d" />

## Setting Up Apache Spark Environment

### Verifying the Spark Docker Container

   **Run the Apache Spark Docker Container**
   ```bash
   docker run -it --rm apache/spark-py /bin/bash
   ```

   The output confirms the container is running:

   <img width="1169" alt="Screenshot 2024-12-14 at 1 19 48 AM" src="https://github.com/user-attachments/assets/3ed55765-40d4-4acb-9219-347fde0ebde8" />

   **Verify Spark Version**

   Re-run the version command: **spark-submit --version**

   <img width="702" alt="Screenshot 2024-12-14 at 1 20 04 AM" src="https://github.com/user-attachments/assets/b87ef70f-7502-476b-8dba-d33ae4ed16a3" />

## Copying Files to the Docker Container

To transfer necessary files (EDA_netflix.py and netflix_titles.csv) into the container:

<img width="1271" alt="Screenshot 2024-12-14 at 1 36 00 AM" src="https://github.com/user-attachments/assets/7fd00c37-271a-46df-b2b8-0c1c6320745f" />

### Docker image created visible on Docker UI

<img width="1680" alt="Screenshot 2024-12-14 at 1 36 06 AM" src="https://github.com/user-attachments/assets/5583ff36-6f1a-4136-9c74-20042bd55cf3" />

### Verified Files have been transfered to Container

<img width="564" alt="Screenshot 2024-12-14 at 1 37 34 AM" src="https://github.com/user-attachments/assets/1f044f18-f604-4fbb-a0b6-d3d69ac52a40" />


# Running the Script in Docker(Click Raw option to see the output correctly)

To execute the EDA script, the following command was used by me:

Command:
**/opt/spark/bin/spark-submit --driver-memory 2G --executor-memory 2G /opt/spark/work-dir/EDA_netflix.py**

The output from the Spark job includes the following information:

## 1. Total records: The total number of rows in the dataset (8809 in this case).
 |-- show_id: string (nullable = true)
 |-- type: string (nullable = true)
 |-- title: string (nullable = true)
 |-- director: string (nullable = true)
 |-- cast: string (nullable = true)
 |-- country: string (nullable = true)
 |-- date_added: string (nullable = true)
 |-- release_year: string (nullable = true)
 |-- rating: string (nullable = true)
 |-- duration: string (nullable = true)
 |-- listed_in: string (nullable = true)
 |-- description: string (nullable = true)

Total records: 8809
+-------+-------+--------------------+--------------------+--------------------+--------------------+------------------+------------+------+---------+--------------------+--------------------+
|show_id|   type|               title|            director|                cast|             country|        date_added|release_year|rating| duration|           listed_in|         description|
+-------+-------+--------------------+--------------------+--------------------+--------------------+------------------+------------+------+---------+--------------------+--------------------+
|     s1|  Movie|Dick Johnson Is Dead|     Kirsten Johnson|                null|       United States|September 25, 2021|        2020| PG-13|   90 min|       Documentaries|As her father nea...|
|     s2|TV Show|       Blood & Water|                null|Ama Qamata, Khosi...|        South Africa|September 24, 2021|        2021| TV-MA|2 Seasons|International TV ...|After crossing pa...|
|     s3|TV Show|           Ganglands|     Julien Leclercq|Sami Bouajila, Tr...|                null|September 24, 2021|        2021| TV-MA| 1 Season|Crime TV Shows, I...|To protect his fa...|
|     s4|TV Show|Jailbirds New Orl...|                null|                null|                null|September 24, 2021|        2021| TV-MA| 1 Season|Docuseries, Reali...|Feuds, flirtation...|
|     s5|TV Show|        Kota Factory|                null|Mayur More, Jiten...|               India|September 24, 2021|        2021| TV-MA|2 Seasons|International TV ...|In a city of coac...|
|     s6|TV Show|       Midnight Mass|       Mike Flanagan|Kate Siegel, Zach...|                null|September 24, 2021|        2021| TV-MA| 1 Season|TV Dramas, TV Hor...|The arrival of a ...|
|     s7|  Movie|My Little Pony: A...|Robert Cullen, Jo...|Vanessa Hudgens, ...|                null|September 24, 2021|        2021|    PG|   91 min|Children & Family...|Equestria's divid...|
|     s8|  Movie|             Sankofa|        Haile Gerima|Kofi Ghanaba, Oya...|United States, Gh...|September 24, 2021|        1993| TV-MA|  125 min|Dramas, Independe...|On a photo shoot ...|
|     s9|TV Show|The Great British...|     Andy Devonshire|Mel Giedroyc, Sue...|      United Kingdom|September 24, 2021|        2021| TV-14|9 Seasons|British TV Shows,...|A talented batch ...|
|    s10|  Movie|        The Starling|      Theodore Melfi|Melissa McCarthy,...|       United States|September 24, 2021|        2021| PG-13|  104 min|    Comedies, Dramas|A woman adjusting...|
+-------+-------+--------------------+--------------------+--------------------+--------------------+------------------+------------+------+---------+--------------------+--------------------+
only showing top 10 rows


## 2. A table showing the number of missing values in each column and the percentage of missing values relative to the total number of rows.

Missing values in each column:
+-------+----+-----+--------+----+-------+----------+------------+------+--------+---------+-----------+
|show_id|type|title|director|cast|country|date_added|release_year|rating|duration|listed_in|description|
+-------+----+-----+--------+----+-------+----------+------------+------+--------+---------+-----------+
|      0|   1|    2|    2636| 826|    832|        13|           2|     6|       5|        3|          3|
+-------+----+-----+--------+----+-------+----------+------------+------+--------+---------+-----------+

Missing value percentages:
+-------+--------------------+--------------------+------------------+----------------+-----------------+------------------+--------------------+------------------+-------------------+------------------+------------------+
|show_id|                type|               title|          director|            cast|          country|        date_added|        release_year|            rating|           duration|         listed_in|       description|
+-------+--------------------+--------------------+------------------+----------------+-----------------+------------------+--------------------+------------------+-------------------+------------------+------------------+
|    0.0|0.011352026336701102|0.022704052673402204|29.923941423544104|9.37677375411511|9.444885912135316|0.1475763423771143|0.022704052673402204|0.0681121580202066|0.05676013168350551|0.0340560790101033|0.0340560790101033|
+-------+--------------------+--------------------+------------------+----------------+-----------------+------------------+--------------------+------------------+-------------------+------------------+------------------+

+-------+--------------------+-------------+---------------------------------+--------------------+--------------------+----------------+---------------+-----------------+-----------------+-------------+--------------------+--------------------+
## 3. A table summarizing various statistics for each column, including:
count: The number of non-null values.
mean: The average value (applicable to numeric columns).
stddev: The standard deviation (applicable to numeric columns).
min: The minimum value.
max: The maximum value.

+-------+--------------------+-------------+---------------------------------+--------------------+--------------------+----------------+---------------+-----------------+-----------------+-------------+--------------------+--------------------+
|summary|             show_id|         type|                            title|            director|                cast|         country|     date_added|     release_year|           rating|     duration|           listed_in|         description|
+-------+--------------------+-------------+---------------------------------+--------------------+--------------------+----------------+---------------+-----------------+-----------------+-------------+--------------------+--------------------+
|  count|                8809|         8808|                             8807|                6173|                7983|            7977|           8796|             8807|             8803|         8804|                8806|                8806|
|   mean|                null|         null|               1124.7692307692307|                null|                null|          1944.0|           null|2014.189598270172|           2016.8|       1994.0|                null|  2014.6666666666667|
| stddev|                null|         null|               1042.1800991068478|                null|                null|            null|           null|8.786618147271653|6.260990336999442|         null|                null|   4.509249752822894|
|    min| and probably will."|        Movie|             "Behind ""The Cov...|"Sam ""Blitz"" Ba...|"Black Deniro, By...| Ama K. Abebrese| April 15, 2018|   Charles Rocket|    Adriane Lenox| Alan Cumming|          Akin Lewis|      Alicia Sánchez|
|    max|                s999|William Wyler|최강전사 미니특공대 : 영웅의 탄생|        Şenol Sönmez|Ṣọpẹ́ Dìrísù, Wun...|        Zimbabwe|  United States|    United States|               UR|United States|United States, Un...|“Last Chance U” h...|
+-------+--------------------+-------------+---------------------------------+--------------------+--------------------+----------------+---------------+-----------------+-----------------+-------------+--------------------+--------------------+


## 4. A list of all unique values found in the "type" column.

Unique types:
+-------------+
|         type|
+-------------+
|         null|
|      TV Show|
|        Movie|
|William Wyler|
+-------------+
## 5. A table showing the number of entries for each unique value in the "type" column.

Distribution by type:
+-------------+-----+
|         type|count|
+-------------+-----+
|         null|    1|
|      TV Show| 2676|
|        Movie| 6131|
|William Wyler|    1|
+-------------+-----+

## 6. A table showing the top 10 countries with the most entries in the "country" column.


Top 10 countries with the most entries:
+--------------+-----+
|       country|count|
+--------------+-----+
| United States| 2805|
|         India|  972|
|          null|  832|
|United Kingdom|  419|
|         Japan|  245|
|   South Korea|  199|
|        Canada|  181|
|         Spain|  145|
|        France|  123|
|        Mexico|  110|
+--------------+-----+
only showing top 10 rows

## 7. A table showing a sample of the "release_year" distribution (top 10 rows).

Release year trend:
+-----------------+-----+
|     release_year|count|
+-----------------+-----+
|    United States|    1|
|    June 12, 2021|    1|
| January 15, 2021|    1|
| January 13, 2021|    1|
|December 15, 2020|    1|
|  August 13, 2020|    1|
|           40 min|    1|
|             2021|  589|
|             2020|  952|
|             2019| 1026|
+-----------------+-----+
only showing top 10 rows

## 8. A sample of the data for US movies, showing the same columns as the original data sample.

Sample of US Movies:
+-------+-----+--------------------+----------------+--------------------+-------------+------------------+------------+------+--------+--------------------+--------------------+
|show_id| type|               title|        director|                cast|      country|        date_added|release_year|rating|duration|           listed_in|         description|
+-------+-----+--------------------+----------------+--------------------+-------------+------------------+------------+------+--------+--------------------+--------------------+
|     s1|Movie|Dick Johnson Is Dead| Kirsten Johnson|                null|United States|September 25, 2021|        2020| PG-13|  90 min|       Documentaries|As her father nea...|
|    s10|Movie|        The Starling|  Theodore Melfi|Melissa McCarthy,...|United States|September 24, 2021|        2021| PG-13| 104 min|    Comedies, Dramas|A woman adjusting...|
|    s28|Movie|           Grown Ups|    Dennis Dugan|Adam Sandler, Kev...|United States|September 20, 2021|        2010| PG-13| 103 min|            Comedies|Mourning the loss...|
|    s29|Movie|          Dark Skies|   Scott Stewart|Keri Russell, Jos...|United States|September 19, 2021|        2013| PG-13|  97 min|Horror Movies, Sc...|A family’s idylli...|
|    s42|Movie|                Jaws|Steven Spielberg|Roy Scheider, Rob...|United States|September 16, 2021|        1975|    PG| 124 min|Action & Adventur...|When an insatiabl...|
+-------+-----+--------------------+----------------+--------------------+-------------+------------------+------------+------+--------+--------------------+--------------------+
only showing top 5 rows







