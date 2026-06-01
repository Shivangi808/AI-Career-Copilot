# helpers.py

# ---------------- SKILL DATABASE ----------------

skills_db = [

    # Programming
    "python",
    "java",
    "c++",
    "javascript",

    # AI / ML
    "machine learning",
    "deep learning",
    "tensorflow",
    "pytorch",
    "scikit-learn",
    "nlp",
    "computer vision",
    "generative ai",

    # Data
    "sql",
    "mysql",
    "postgresql",
    "pandas",
    "numpy",
    "data analysis",
    "power bi",
    "excel",
    "tableau",

    # Web / Frameworks
    "html",
    "css",
    "react",
    "node.js",
    "flask",
    "django",
    "streamlit",

    # Tools / Cloud
    "git",
    "github",
    "docker",
    "linux",
    "aws",
    "google colab"
]


# ---------------- EXTRACT SKILLS ----------------

def extract_skills(text):

    text = text.lower()
    found_skills = []

    for skill in skills_db:
        if skill in text:
            found_skills.append(skill)

    return list(set(found_skills))


# ---------------- FIND MISSING ----------------

def find_missing_skills(resume_skills, jd_skills):

    missing = []

    for skill in jd_skills:
        if skill not in resume_skills:
            missing.append(skill)

    return missing


# ---------------- LEARNING RECOMMENDATIONS ----------------

def learning_recommendations(missing_skills):

    recommendations = {

        "python":
        "Practice Python basics, OOP, functions and problem solving.",

        "java":
        "Practice OOP, collections, exception handling and Java applications.",

        "c++":
        "Strengthen STL, OOP and problem solving using C++.",

        "javascript":
        "Learn DOM manipulation, ES6 and interactive web development.",

        "machine learning":
        "Study supervised and unsupervised learning concepts and build ML models.",

        "scikit-learn":
        "Learn model training, preprocessing and evaluation using Scikit-learn.",

        "sql":
        "Practice SQL queries, joins, aggregation and database concepts.",

        "mysql":
        "Practice schema design, queries and database management using MySQL.",

        "postgresql":
        "Learn relational databases and advanced SQL using PostgreSQL.",

        "pandas":
        "Learn dataframe operations, cleaning and analysis using Pandas.",

        "numpy":
        "Learn array operations and numerical computing with NumPy.",

        "deep learning":
        "Study neural networks, CNNs and deep learning architectures.",

        "tensorflow":
        "Build and train deep learning models using TensorFlow.",

        "pytorch":
        "Practice deep learning workflows and model building using PyTorch.",

        "data analysis":
        "Practice EDA, visualization and extracting insights from datasets.",

        "html":
        "Learn webpage structure and semantic HTML fundamentals.",

        "css":
        "Practice layouts, responsiveness and modern styling.",

        "react":
        "Build component-based front-end projects using React.",

        "node.js":
        "Learn server-side JavaScript and API development using Node.js.",

        "flask":
        "Build Python backend applications and REST APIs using Flask.",

        "django":
        "Learn full-stack web development using Django.",

        "streamlit":
        "Build interactive data and AI applications using Streamlit.",

        "git":
        "Learn version control, commits, branching and Git workflows.",

        "github":
        "Practice repositories, pushes, pull requests and deployment.",

        "docker":
        "Learn containerization and application deployment using Docker.",

        "linux":
        "Practice command line operations and Linux workflows.",

        "aws":
        "Learn cloud deployment and AWS core services.",

        "power bi":
        "Build dashboards and learn business intelligence workflows.",

        "excel":
        "Practice formulas, pivot tables and spreadsheet analysis.",

        "tableau":
        "Create visual dashboards and data storytelling projects.",

        "nlp":
        "Learn text processing, embeddings and NLP pipelines.",

        "computer vision":
        "Study image processing and computer vision models.",

        "generative ai":
        "Build LLM and generative AI projects using modern AI tools."
    }

    result = {}

    for skill in missing_skills:

        if skill in recommendations:
            result[skill] = recommendations[skill]

        else:
            result[skill] = (
                "Explore beginner resources and build projects in this skill."
            )

    return result


# ---------------- RESUME IMPROVEMENTS ----------------

def resume_improvements(missing_skills):

    suggestions = {}

    for skill in missing_skills:

        suggestions[skill] = (
            f"Consider adding projects, coursework, or practical experience related to {skill} in your resume."
        )

    return suggestions