APP_TITLE = "Web Portofolio"

APP_INTRO = """This is a demonstration app that shows a developer's Portfolio."""

APP_HOW_IT_WORKS = """This app provides developer a basic and standard web portfolio template. which has professional details about a developer.
this portfolio will contain details about developer, educational details,contact details, certfications, hobbies and intrests, projects, internships and work experience.
"""
SHARED_ASSET = {}

HTML_BUTTON = {}

user_cred = {
    "name" : "bhuvan",
    "body" : "test"
}

PHASES = {
    "phase1": {
        "name": "About Me",
        "fields": {
            "about_me": {
                "type": "markdown",
                "body": name,
                "unsafe_allow_html": bool(1)
             },
            "image": {
                "type": "image",
                "image": "no_pic.jpeg",
                "caption": "My Image",
            },
            "edu_det": {
                "type": "markdown",
                "body": body,
                "unsafe_allow_html": bool(1)
            }
            # "day": {
            #     "type": "number_input",
            #     "label": "What is your birth day?",
            #     "min_value": 1,
            #     "max_value": 31,
            #     "showIf": {"system": "Western"}
            # },
            # "year": {
            #     "type": "number_input",
            #     "label": "What is your birth year?",
            #     "min_value": 1900,
            #     "max_value": 2020,
            #     "showIf": {"system": ["Western", "Chinese"]}
            # }
        }
    }
}

PREFERRED_LLM = "gpt-4o-mini"
LLM_CONFIG_OVERRIDE = {}

SCORING_DEBUG_MODE = True
DISPLAY_COST = True

COMPLETION_MESSAGE = "You've reached the end! I hope you learned something!"
COMPLETION_CELEBRATION = False

