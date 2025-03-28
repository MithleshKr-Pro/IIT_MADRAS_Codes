import random
def generate_student_data(n_students, courses, cities, random_seed=42):
    '''
    Create a list of dict with dictionaries representing each attributes of each student.
    '''
    random.seed(random_seed)
    return [
      {
        "rollno": i, "city": random.choice(cities), 
        **{course: random.randint(1,100) for course in courses} 
      }
      for i in range(1,n_students+1)
    ]

def groupby(data:list, key:callable):
    '''
    Given a list of items, and a key, create a dictionary with the key as key function called 
    on item and the list of items with the same key as the corresponding value. 
    The order of items in the group should be the same order in the original list
    '''
    ...

def apply_to_groups(groups:dict, func:callable):
    '''
    Apply a function to the list of items for each group.
    '''
    ...

def min_course_marks(student_data, course):
    '''Return the min marks on a given course'''
    ...

def max_course_marks(student_data, course):
    '''Return the max marks on a given course'''
    ...

def rollno_of_max_marks(student_data, course):
    '''Return the rollno of student with max marks in a course'''
    ...

def sort_rollno_by_marks(student_data, course1, course2, course3):
    '''
    Return a sorted list of rollno sorted based on their marks on the three course marks. 
    course1 is compared first, then course2, then course3 to break ties.
    Hint: use tuples comparision
    '''
    ...

def count_students_by_cities(student_data):
    '''
    Create a dictionary with city as key and number of students from each city as value.
    '''
    ...

def city_with_max_no_of_students(student_data):
    '''
    Find the city with the maximum number of students.
    '''
    ...

def group_rollnos_by_cities(student_data):
    '''
    Create a dictionary with city as key and 
    a sorted list of rollno of students that belong to 
    that city as the value.
    '''
    ...

def city_with_max_avg_course_mark(student_data, course):
    '''
    Find the city with the maximum avg course marks.
    '''
    ...











import random
def generate_student_data(n_students, courses, cities, random_seed=42):
    '''
    Create a list of dict with dictionaries representing each attributes of each student.
    '''
    random.seed(random_seed)
    return [
      {
        "rollno": i, "city": random.choice(cities), 
        **{course: random.randint(1,100) for course in courses} 
      }
      for i in range(1,n_students+1)
    ]

from collections import defaultdict
from collections import Counter

def groupby(data:list, key:callable):
    '''
    Given a list of items, and a key, create a dictionary with the key as key function called 
    on item and the list of items with the same key as the corresponding value. 
    The order of items in the group should be the same order in the original list
    '''
    groups = defaultdict(list)
    for item in data:
        groups[key(item)].append(item)
    return dict(groups)

def apply_to_groups(groups:dict, func:callable):
    '''
    Apply a function to the list of items for each group.
    '''
    
    return {key: func(value) for key, value in groups.items()}

def min_course_marks(student_data, course):
    '''Return the min marks on a given course'''
    
    return min(student[course] for student in student_data)

def max_course_marks(student_data, course):
    '''Return the max marks on a given course'''
    
    return max(student[course] for student in student_data)

def rollno_of_max_marks(student_data, course):
    '''Return the rollno of student with max marks in a course'''
    
    return max(student_data, key=lambda student: student[course])["rollno"]

def sort_rollno_by_marks(student_data, course1, course2, course3):
    '''
    Return a sorted list of rollno sorted based on their marks on the three course marks. 
    course1 is compared first, then course2, then course3 to break ties.
    Hint: use tuples comparision
    '''
    
    
    return [student["rollno"] for student in sorted(
        student_data,
        key=lambda s: (-s[course1], -s[course2], -s[course3], s["rollno"])
    )]

def count_students_by_cities(student_data):
    '''
    Create a dictionary with city as key and number of students from each city as value.
    '''
    # city_count = defaultdict(int)
    # for student in student_data:
    #     city_count[student["city"]] += 1
    # return dict(city_count)
    return dict(Counter(map(lambda s: s["city"], student_data)))

def city_with_max_no_of_students(student_data):
    '''
    Find the city with the maximum number of students.
    '''
    city_count = count_students_by_cities(student_data)
    return max(city_count, key=city_count.get)

def group_rollnos_by_cities(student_data):
    '''
    Create a dictionary with city as key and 
    a sorted list of rollno of students that belong to 
    that city as the value.
    '''
    city_groups = groupby(student_data, lambda s: s["city"])
    return {city: sorted([s["rollno"] for s in students]) for city, students in city_groups.items()}


def city_with_max_avg_course_mark(student_data, course):
    '''
    Find the city with the maximum avg course marks.
    '''
    city_groups = groupby(student_data, lambda s: s["city"])
    city_avg = {city: sum(s[course] for s in students) / len(students) for city, students in city_groups.items()}
    return max(city_avg, key=city_avg.get)
