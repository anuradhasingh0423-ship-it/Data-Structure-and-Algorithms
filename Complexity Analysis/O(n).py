def find_paper(papers, name):
    for paper in papers:
        if paper == name:
            return True
    return False

papers = ["Anuradha", "Rohit", "Aradhya", "Teena", "Kusum"]

search_name = "Rohit"

result = find_paper(papers, search_name)

if result:
    print("Found")
else:
    print("Not found")