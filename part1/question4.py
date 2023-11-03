import pets_db

################################################################################
#     ____                          __     _                          __ __
#    / __ \  __  __  ___    _____  / /_   (_)  ____    ____          / // /
#   / / / / / / / / / _ \  / ___/ / __/  / /  / __ \  / __ \        / // /_
#  / /_/ / / /_/ / /  __/ (__  ) / /_   / /  / /_/ / / / / /       /__  __/
#  \___\_\ \__,_/  \___/ /____/  \__/  /_/   \____/ /_/ /_/          /_/   
#                                                                          
#  Question 4
################################################################################
#
# Instructions:
# Question 4 and Question 5 are about writing SQL. THey use the database that is 
# created in the file `pets_db.py`. 
# These questions use a database called SQLite. You do not need to install anything.
# In the file `pets_db.py` three tables are created. Data is then added to each 
# of the tables. The questions below are about how the data in each of the tables
# is related.

# Part 4.A:
# Write SQL to select the pets that are owned by nobody.
# The output should be a list of tuples in the format: (<pet name>, <species>, <age>)

sql_pets_owned_by_nobody = """

select  animals.name, animals.species,animals.age from animals left join people_animals on 
animals.animal_id = people_animals.pet_id 
where people_animals.pet_id is null

"""
pets_db.create_db()

with pets_db.get_connection() as con:
    res = con.execute(sql_pets_owned_by_nobody)
    result = res.fetchall()
    print(result)

# Part 4.B:
# Write SQL to select how the number of pets are older than their owners. 
# The output should be an integer.

sql_pets_older_than_owner = """

select count(people_animals.owner_id) from people_animals inner join 
people ON people.person_id = people_animals.owner_id inner join
animals ON animals.animal_id = people_animals.pet_id where animals.age > people.age

"""


# Part 4.C: BONUS CHALLENGE! 
# Write SQL to select the pets that are owned by Bessie and nobody else.
# The output should be a list of tuples in the format: (<person name>, <pet name>, <species>)
sql_only_owned_by_bessie = """ 

select distinct people.name, animals.name, animals.species from people_animals INNER JOIN 
Animals ON people_animals.pet_id = animals.animal_id INNER JOIN 
people ON people.person_id = people_animals.owner_id 
where people.name = 'bessie' and animals.animal_id NOT IN 
(select pet_id from people_animals inner join
People ON people_animals.owner_id = people.person_id where people.name <> 'bessie')

"""
