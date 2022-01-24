
captital ={
    "France": "Paris",
    "Germany": "Berlin",
}
#nesting Dict in List
travel_log = {
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": ["berlin", "Hamburg", "Styttgart"]
}
#nesting Dict in Dict
travel_dic = {
    "France": {"cities_visited":["Paris","Lille","Dijon"],"total_visited":0},
    "Korea": {"cities_visited":["seoul","busan","jeju"],"total_visited": 10},
}
#nesting List in Dict
travel_list = [
    {"country": "France",
     "cities_visited":["Paris","Lille","Dijon"],
     "total_visited":0},
    {"country": "Korea",
     "cities_visited":["seoul","busan","jeju"],
     "total_visited": 10},
]
#새로운 사전형을 기존의 사전형에 추가하기 위한 함수
def add_new_country(add_country, add_visited_cities, add_visited_time):
    #추가할 사전형은 리스트에 사전형이 중첩되어 있기에 빈 사전형을 생성한후 키:밸류 를 추가해준다
    new_country = {}
    new_country["country"] = add_country
    new_country["cities_visited"] = add_visited_cities
    new_country["total_visited"] = add_visited_time
    #기존의 사전형은 리스트 이기에 리스트의 끝단에 추가할수있는 append를 사용하여 추가해준다
    travel_list.append(new_country)

add_new_country("Russia", ["Moscow", "Saint Petersburg"],2)
print(travel_list)

