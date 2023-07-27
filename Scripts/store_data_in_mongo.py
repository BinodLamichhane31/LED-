import pymongo

team_data = {
    "churchboys": [
        {
            "name": "Ananta Tamang (captain)",
            "essay": "Ananta Tamang (Nepali: अनन्त तामाङ; born 14 January 1998) is a Nepalese professional footballer who plays as a defender for Nepal Super League club church boys united[3] and the Nepal national team. He was vice-captain of Nepal under-19 football team which went on to win the 2015 SAFF U-19 Championship. Tamang made his senior national team debut on 31 August 2015 in a friendly against India.[4]",
            "description": "Church Boys United (formally known as Church Boys FC) is a Nepali football team from balkumari neighborhood of Lalitpur that competes in the Martyr's Memorial A-Division League. The team was first promoted to Martyr's Memorial A-Division League in 2022, having won the 2022 Martyr's Memorial B-Division League."
        },
        {
            "name": "Saugat Shahi",
            "essay": "Saugat Shahi is a talented midfielder...",
            "description": "The club was founded in 2009, but only participated in local tournaments. In 2019, they qualified for the Martyr's Memorial C-Division League which was their fifth attempt in C-Division League Qualifier (previously known as Martyr's Memorial 'D' Division League)[citation needed] and were promoted to the top-level Martyr's Memorial A-Division League within two seasons, in what The Kathmandu Post highlighted as a 'remarkable journey'."
        },
        {
            "name": "Biswas Shrestha",
            "essay": "Biswas Shrestha is a young and promising striker...",
            "description": "Hi"
        },
        {
            "name": "Biswas Shrestha",
            "essay": "Biswas Shrestha is a young and promising striker...",
            "description": "Hi"
        },
        {
            "name": "Biswas Shrestha",
            "essay": "Biswas Shrestha is a young and promising striker...",
            "description": "Hi"
        },
        {
            "name": "Biswas Shrestha",
            "essay": "Biswas Shrestha is a young and promising striker...",
            "description": "Hi"
        },
        {
            "name": "Biswas Shrestha",
            "essay": "Biswas Shrestha is a young and promising striker...",
            "description": "Hi"
        },
        {
            "name": "Biswas Shrestha",
            "essay": "Biswas Shrestha is a young and promising striker...",
            "description": "Hi"
        },
        {
            "name": "Biswas Shrestha",
            "essay": "Biswas Shrestha is a young and promising striker...",
            "description": "Hi"
        },
        {
            "name": "Biswas Shrestha",
            "essay": "Biswas Shrestha is a young and promising striker...",
            "description": "Hi"
        },
        {
            "name": "Biswas Shrestha",
            "essay": "Biswas Shrestha is a young and promising striker...",
            "description": "Hi"
        },
        {
            "name": "Biswas Shrestha",
            "essay": "Biswas Shrestha is a young and promising striker...",
            "description": "Hi"
        },
        {
            "name": "Biswas Shrestha",
            "essay": "Biswas Shrestha is a young and promising striker...",
            "description": "Hi"
        },
        {
            "name": "Biswas Shrestha",
            "essay": "Biswas Shrestha is a young and promising striker...",
            "description": "Hi"
        },
        {
            "name": "Biswas Shrestha",
            "essay": "Biswas Shrestha is a young and promising striker...",
            "description": "Hi"
        }
    ],
    "newroad": [
        {
            "name": "John Doe",
            "essay": "John Doe is a skilled defender...",
            "description": ""
        },
        {
            "name": "Jane Doe",
            "essay": "Jane Doe is a versatile midfielder...",
            "description": ""
        },
        {
            "name": "Michael Smith",
            "essay": "Michael Smith is a goal-scoring forward...",
            "description": ""
        }
    ]
   
}

def store_data_in_mongo():
    mongo_url = "mongodb://localhost:27017"
    client = pymongo.MongoClient(mongo_url)
    db = client["team"]
    collection = db["team_data"]

    for team_name, team_details in team_data.items():
        team_doc = {
            "name": team_name,
            "details": team_details
        }
        collection.insert_one(team_doc)

if __name__ == "__main__":
    store_data_in_mongo()
