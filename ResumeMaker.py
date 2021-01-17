def RESUME_MAKER():
    full_name = input('What is your full name: ')
    #job = input('What is your job Title: ')
    email = input('What is your email address: ')
    phone = input('What is your phone number: ')
    #address = input('What is your address: ')
    #website = input('What is your website URL (optional): ')
    linkedIn = input('What is your linkedIn link (optional): ')
    github = input('What is your github link (optional): ')

    Prereqs = r"""\documentclass[A4,11pt]{article}
    \usepackage{latexsym}
    \usepackage[empty]{fullpage}
    \usepackage{titlesec}
    \usepackage{marvosym}
    \usepackage[usenames,dvipsnames]{color}
    \usepackage{verbatim}
    \usepackage{enumitem}
    \usepackage[hidelinks]{hyperref}
    \usepackage[english]{babel}
    \usepackage{tabularx}
    \usepackage{tikz}
    \input{glyphtounicode}


    \usepackage{palatino}

    \addtolength{\oddsidemargin}{-1cm}
    \addtolength{\evensidemargin}{-1cm}
    \addtolength{\textwidth}{2cm}
    \addtolength{\topmargin}{-1cm}
    \addtolength{\textheight}{2cm}

    \urlstyle{same}

    \raggedbottom
    \raggedright
    \setlength{\tabcolsep}{0cm}

    \titleformat{\section}{
      \vspace{-4pt}\scshape\raggedright\large
    }{}{0em}{}[\color{black}\titlerule \vspace{-5pt}]

    \pdfgentounicode=1

    \newcommand{\CVItem}[1]{
      \item\small{
        {#1 \vspace{-2pt}}
      }
    }

    \newcommand{\CVSubheading}[4]{
      \vspace{-2pt}\item
        \begin{tabular*}{0.97\textwidth}[t]{l@{\extracolsep{\fill}}r}
          \textbf{#1} & #2 \\
          \small#3 & \small #4 \\
        \end{tabular*}\vspace{-7pt}
    }

    \newcommand{\CVSubSubheading}[2]{
        \item
        \begin{tabular*}{0.97\textwidth}{l@{\extracolsep{\fill}}r}
          \text{\small#1} & \text{\small #2} \\
        \end{tabular*}\vspace{-7pt}
    }

    \newcommand{\CVSubItem}[1]{\CVItem{#1}\vspace{-4pt}}

    \renewcommand\labelitemii{$\vcenter{\hbox{\tiny$\bullet$}}$}

    \newcommand{\CVSubHeadingListStart}{\begin{itemize}[leftmargin=0.5cm, label={}]}

    \newcommand{\CVSubHeadingListEnd}{\end{itemize}}
    \newcommand{\CVItemListStart}{\begin{itemize}}
    \newcommand{\CVItemListEnd}{\end{itemize}\vspace{-5pt}}"""

    Header = r""" \begin{center}
        \textbf{\Huge \scshape [[full_name]]} \\ \vspace{1pt} %\scshape sets small capital letters, remove if desired
        \small [[phone]] $|$ 
        \href{mailto:[[email]]}{\underline{[[email]]}} $|$\\
        \href{https:[[linkedIn]]}{\underline{[[linkedIn]]}} $|$
        \href{https:[[github]]}{\underline{[[github]]}}
    \end{center}""".replace("[[full_name]]", full_name).replace("[[phone]]", phone).replace("[[email]]", phone).replace("[[linkedIn]]", linkedIn).replace("[[github]]", github)

    Education_entries = []
    Work_entries = []
    Project_entries = []
    Skills_entries = []

    def add_education():
        Degree = input('What Degree did you achieve: ')
        Degree_detail = input('Any Minor detail on degree? (Ex: Majors and Minors):')
        Start_date = input('When did you start? (Format: Month Abbreviation. YEAR [ex: Aug. 2020]): ')
        End_date = input('When did you complete your education? (Format: Month Abbreviation. YEAR [ex: Aug. 2020]) If studying press enter: ')
        Institute = input('Which institute did you study in?: ')
        Location = input('Where did you study?:')
        if End_date == "":
            End_date = 'Present'
        education_header = r"""    \CVSubheading
          {{[[DEGREE]]} $|$ \emph{\small{[[MINOR DETAIL]]}}}{[[START]] -- [[STOP]]}
          {[[INSTITUTE]]}{[[LOCATION]]}""".replace('[[DEGREE]]', Degree).replace('[[MINOR DETAIL]]', Degree_detail).replace('[[START]]', Start_date).replace('[[STOP]]', End_date).replace('[[INSTITUTE]]', Institute).replace('[[LOCATION]]', Location)
        Education_entries.append(education_header)

    def add_work():
        Title = input('What was your Job Title: ')
        Start_date = input('When did you start? (Format: Month Abbreviation. YEAR [ex: Aug. 2020]): ')
        End_date = input('When did you complete your work? (Format: Month Abbreviation. YEAR [ex: Aug. 2020]) If working here press enter: ')
        Company = input('Which Company did you work for?: ')
        Location = input('Where did you work?:')
        work_header = r"""    \CVSubheading 
          {[[TITLE]]}{[[START]] -- [[STOP]]}
          {[[COMPANY]]}{[[LOCATION]]}""".replace('[[TITLE]]', Title).replace('[[START]]', Start_date).replace('[[STOP]]', End_date).replace('[[COMPANY]]', Company).replace('[[LOCATION]]', Location)
        Details = input("Why it is important to this employer? Write in Bullets with new bullets at every ';' :")
        Details = Details.split(';')
        Details_in_format = ''
        for i in Details:
            Details_in_format = Details_in_format+ "\n" + '\CVItem{' + i + '}'
        work_details = r"""
          \CVItemListStart""" + "\n" + Details_in_format + "\n" + r"""\CVItemListEnd"""
        work_header = work_header + work_details
        Work_entries.append(work_header)

    def add_project():
        Title = input('What was your Project/Research Title: ')
        Minor_Detail = input('Any minor detail on your project? (Ex: Which language used?)')
        Project_date = input('When did you complete it? (Format: Month Abbreviation. YEAR [ex: Aug. 2020]): ')
        Institute = input("Which institute did you work in for? If by yourself type 'Personal': ")
        project_header = r"""    \CVSubheading
          {{[[TITLE]]} $|$ \emph{\small{[[MINOR_DETAIL]]}}}{[[DATE]]}
          {[[INSTITUTE]]}{}""".replace('[[TITLE]]', Title).replace('[[MINOR_DETAIL]]', Minor_Detail).replace('[[DATE]]', Project_date).replace('[[INSTITUTE]]', Institute)
        Project_entries.append(project_header)

    def add_skills():
        Skill = input('What are you skilled at?: ')
        Info = input('Elaborate a bit more on your Skill: ')
        skill_info = r"\textbf{[[SKILL]]}{: [[DETAILS]]}".replace('[[SKILL]]', Skill).replace('[[DETAILS]]', Info)
        Skills_entries.append(skill_info)

    Education = r"""\section{Education}
      \CVSubHeadingListStart
      [[Education Details]]
      \CVSubHeadingListEnd"""

    Work = r"""\section{Work Experience}
      \CVSubHeadingListStart
        [[Work Details]]
      \CVSubHeadingListEnd
    """

    Projects = r"""\section{Projects and Research}
      \CVSubHeadingListStart
        [[Project Details]]
      \CVSubHeadingListEnd"""

    Skills = r"""\section{Skills}
     \begin{itemize}[leftmargin=0.5cm, label={}]
        \small{\item{
         [[Skill Details]]
        }}
     \end{itemize}"""

    while True:
        if input('Add an entry to Education? (at least 1 required) (Y/N): ').lower() == 'n':
            break
        else:
            add_education()
            if input('Keep adding entries? (Y/N): ').lower() == 'n':
                break
            else:
                pass

    while True:
        if input('Add an entry to Work? (at least 1 required) (Y/N): ').lower() == 'n':
            break
        else:
            add_work()
            if input('Keep adding entries? (Y/N): ').lower() == 'n':
                break
            else:
                pass

    while True:
        if input('Add an entry to Projects/Research? (at least 1 required) (Y/N): ').lower() == 'n':
            break
        else:
            add_project()
            if input('Keep adding entries? (Y/N): ').lower() == 'n':
                break
            else:
                pass

    while True:
        if input('Add an entry to Skills? (at least 1 required) (Y/N): ').lower() == 'n':
            break
        else:
            add_skills()
            if input('Keep adding entries? (Y/N): ').lower() == 'n':
                break
            else:
                pass

    def format_text():
        formatted_education_details = ''
        formatted_work_details = ''
        formatted_projects_details = ''
        formatted_skills_details = ''
        for entry in Education_entries:
            formatted_education_details = formatted_education_details + entry +"\n"
        for entry in Work_entries:
            formatted_work_details = formatted_work_details + entry +"\n"
        for entry in Project_entries:
            formatted_projects_details = formatted_projects_details + entry +"\n"
        for entry in Skills_entries:
            formatted_skills_details = formatted_skills_details + entry +"\n"
        formatted_education = Education.replace('[[Education Details]]', formatted_education_details)
        formatted_work = Work.replace('[[Work Details]]', formatted_work_details)
        formatted_projects = Projects.replace('[[Project Details]]', formatted_projects_details)
        formatted_skills = Skills.replace('[[Skill Details]]', formatted_skills_details)
        return formatted_education,  formatted_work, formatted_projects, formatted_skills


    resumaster = open("Dev_Resume.txt","a")
    resumaster.write(Prereqs)
    resumaster.write('\n')
    resumaster.write(r'\begin{document}')
    resumaster.write(Header)
    a, b, c ,d = format_text()
    resumaster.write('\n')
    resumaster.write('\n')
    resumaster.write(a)
    resumaster.write('\n')
    resumaster.write('\n')
    resumaster.write(b)
    resumaster.write('\n')
    resumaster.write('\n')
    resumaster.write(c)
    resumaster.write('\n')
    resumaster.write('\n')
    resumaster.write(d)
    resumaster.write(r'\end{document}')
    resumaster.close()

if __name__ == '__main__':
    RESUME_MAKER()
