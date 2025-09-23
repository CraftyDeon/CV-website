from flask import Flask, render_template

app = Flask(__name__)

# Resume data
resume_data = {
    'name': 'lorem ipsum',
    'job_title': 'Web Developer',
    'contact': {
        'email': 'e@example.com',
        'phone': '1234567890',
        'location': 'City, Country'
    },
    'about': "I'm a passionate web developer with experience in building responsive, user-friendly websites. My strengths lie in front-end development, with a strong command over HTML, CSS, and JavaScript.",
    'experience': [
        {
            'title': 'Front-End Developer',
            'company': 'ABC Company',
            'dates': 'June 2020 - Present',
            'description': 'Developed and maintained the company website using React and Vue.js. Worked on improving user interface performance and accessibility.',
            'image': 'abc_logo.png'  # Place inside static/images/
        },
        {
            'title': 'Web Developer Intern',
            'company': 'XYZ Agency',
            'dates': 'Jan 2019 - May 2020',
            'description': 'Assisted in building responsive websites using HTML5, CSS3, and JavaScript. Collaborated with the design team to ensure seamless user experience.',
            'image': 'xyz_logo.png'  # Place inside static/images/
        }
    ],
    'skills': ['HTML5', 'CSS3', 'JavaScript', 'React', 'Vue.js'],
    'education': {
        'degree': 'B.Sc. in Computer Science',
        'university': 'University of XYZ',
        'graduation_year': '2020',
        'description': 'Graduated with honors. Coursework included Web Development, Algorithms, Data Structures, and Database Management.'
    }
}

# Demo projects per skill
projects_data = {
    'HTML5': ['Portfolio Website', 'Landing Page'],
    'CSS3': ['Responsive Layout', 'Dark Mode Theme'],
    'JavaScript': ['To-Do App', 'Weather Widget'],
    'React': ['Chat App', 'Movie Finder'],
    'Vue.js': ['Task Manager', 'Blog Platform']
}

@app.route("/")
def index():
    return render_template("test.html", data=resume_data)

@app.route("/skills/<skill>")
def skills(skill):
    projects = projects_data.get(skill, [])
    return render_template("skills.html", data=resume_data, skill=skill, projects=projects)

if __name__ == "__main__":
    app.run(debug=True)
