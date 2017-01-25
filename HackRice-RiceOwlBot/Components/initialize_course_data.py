# Write or paste code here. You can also use the blueprints as a starting point.
# -*- coding: utf-8 -*-
from meya import Component

class initialize_course_data(Component):
    def start(self):
        course_data = [
{'subject':'COMP','number':'412',"title":"COMPILER CONSTRUCTION - UG",'location':'DBH 180','description':'''
Topics in the design of programming language translators, including parsing, run-time storage management, error recovery, code generation and optimization.
'''},
{'subject':'COMP','number':'450',"title":"ALGORITHMIC ROBOTICS",'location':'DCH 1064','description':'''
Robots have fascinated people for generations. Today, robots are built for applications as diverse as exploring remote planets, de-mining war zones, cleaning toxic waste, assembling cars, inspecting pipes in industrial plants and mowing lawns. Robots are also interacting with humans in a variety of ways: robots are museum guides, robots assist surgeon sin life threatening operations, and robotic cars can drive us around. The field of robotics studies not only the design of new mechanisms but also the development of artificial intelligence frameworks to make these mechanism useful in the physical world, integrating computer science, engineering, mathematics and more recently biology and sociology, in a unique way. This class will present fundamental algorithmic advances that enable today鈥檚 robots to move in real environments and plan their actions. It will also explore fundamentals of the field of Artificial Intelligence through the prism of robotics. The class involves a si
 gnificant programming project.
'''},
{'subject':'COMP','number':'550',"title":"ALGORITHMIC ROBOTICS",'location':'DCH 1064','description':'''
Robots have fascinated people for generations. Today, robots are built for applications as diverse as exploring remote planets, de-mining war zones, cleaning toxic waste, assembling cars, inspecting pipes in industrial plants and mowing lawns. Robots are also interacting with humans in a variety of ways: robots are museum guides, robots assist surgeon sin life threatening operations, and robotic cars can drive us around. The field of robotics studies not only the design of new mechanisms but also the development of artificial intelligence frameworks to make these mechanism useful in the physical world, integrating computer science, engineering, mathematics and more recently biology and sociology, in a unique way. This class will present fundamental algorithmic advances that enable today鈥檚 robots to move in real environments and plan their actions. It will also explore fundamentals of the field of Artificial Intelligence through the prism of robotics. The class involves a si
 gnificant programming project.
'''},
{'subject':'COMP','number':'515',"title":"ADV COMPILATION VECTOR PARALEL",'location':'KCK 107','description':'''
Advanced compilation techniques for vector and parallel computer systems, including the analysis of program dependence, program transformations to enhance parallelism, compiler management of the memory hierarchy, interprocedural data flow analysis, and parallel debugging.
'''},
{'subject':'COMP','number':'640',"title":"GR SEM IN MACHINE LEARNING",'location':'KCK 107','description':'''
A reading course covering the latest developments in statistical machine learning and pattern recognition.
'''},
{'subject':'COMP','number':'515',"title":"ADV COMPILATION VECTOR PARALEL",'location':'KCK 107','description':'''
Advanced compilation techniques for vector and parallel computer systems, including the analysis of program dependence, program transformations to enhance parallelism, compiler management of the memory hierarchy, interprocedural data flow analysis, and parallel debugging.
'''},
{'subject':'COMP','number':'640',"title":"GR SEM IN MACHINE LEARNING",'location':'KCK 107','description':'''
A reading course covering the latest developments in statistical machine learning and pattern recognition.
'''},
{'subject':'COMP','number':'554',"title":"COMPUTER SYSTEMS ARCHITECTURE",'location':'DCH 1070, DCH 1064','description':'''
Evolution of key architecture concepts found in advanced uniprocessor systems. Fundamental and advanced pipelining techniques and associated issues for improving processor performance. Illustrated with RISC processors such as the ARM processor. Examine several metrics for processor performance, such as Amdahl law. Key concepts of data and program memory systems found in modern systems with memory hierarchies and cashes. Perform experiments in cache performance analysis. Influence of technology trends, such as Moore law, on processor implementation Approaches for exploiting instruction level parallelism, such as VLIW. Introduction to parallel and multicore architectures. Introduction to processor architectures targeted for imbedded applications. Additional coursework required beyond the undergraduate course requirements.
'''},
{'subject':'COMP','number':'501',"title":"PRODUCTION PROGRAMMING",'location':'DCH 1042','description':'''
This course focuses on the principles and practices of test-driven software development, which have been popularized under the banner of "Extreme Programming." To provide students with practical experience, the course engages students in the development of open source production programs written in JAVA or C#. The DRJAVA programming courses was developed by students in this course. Some of the major topics covered in course lectures include design patterns for controlling concurrency and refactoring transformations to improve legacy code.
'''},
{'subject':'COMP','number':'531',"title":"WEB DEVELOPMENT AND DESIGN",'location':'DCH Sym II Lab','description':'''
This project-based course explores Web application creation and design. Students are involved in the development of front-end and back-end systems while interfacting client-server communications technologies. Students will evaluate Web structural frameworks, Web development technologies, apply test driven development, and create multi-user Web applications.
'''},
{'subject':'COMP','number':'582',"title":"GR DESGN ANALY OF ALGORITHMS",'location':'DCH 1055','description':'''
Methods for designing and analyzing computer algorithms and data structures. The focus of this course will be on the theoretical and mathematical aspects of algorithms and data structures.
'''},
{'subject':'COMP','number':'330',"title":"TOOLS & MODELS - DATA SCIENCE",'location':'DCH 1075','description':'''
This course is an introduction to modern data science. Data science is the study of how to extract actionable, non-trivial knowledge from data. The proposed course will focus both on the software tools used by practitioners of modern data science, as well as the mathematical and statistical models that are employed in conjunction with such software tools. On the tools side, we will cover the basics of relational database systems, as well as modern systems for distributed computing based on MapReduce. On the models side, the course will cover standard supervised and unsupervised models for data analysis and pattern discovery.
'''},
{'subject':'COMP','number':'311',"title":"FUNCTIONAL PROGRAMMING",'location':'GRB W212','description':'''
An introduction to concepts, principles, and approaches of functional programming. Functional programming is a style of programming where the key means of computation is the application of functions to arguments (which themselves might be functions). This style of programming has become increasingly popular in recent years because it offers important advantages in designing, maintaining, and reasoning about programs in many modern contexts such as web services, multicore programming, and cluster computing. Course work consists of a series of programming assignments in the Scala programming language and various library extensions such as Apache Spark.
'''},
{'subject':'COMP','number':'504',"title":"GR OBJ-ORIENTED PROG & DESIGN",'location':'OED 112, DCH 1046','description':'''
Discover how stat-of-the-art object-orient programming and design techniques can create globe-spanning software systems that are both flexible and scalable. Learn how software design patterns are used in multiple programming paradigms. Explore highly decoupled systems with dynamically configurable behaviors. Highly recommended for anyone interested in building large systems and software engineering. Basic proficiency in Java is required. Students may not receive credit for both COMP 310/510 and COMP 404/504.
'''},
{'subject':'COMP','number':'311',"title":"FUNCTIONAL PROGRAMMING",'location':'GRB W212','description':'''
An introduction to concepts, principles, and approaches of functional programming. Functional programming is a style of programming where the key means of computation is the application of functions to arguments (which themselves might be functions). This style of programming has become increasingly popular in recent years because it offers important advantages in designing, maintaining, and reasoning about programs in many modern contexts such as web services, multicore programming, and cluster computing. Course work consists of a series of programming assignments in the Scala programming language and various library extensions such as Apache Spark.
'''},
{'subject':'COMP','number':'504',"title":"GR OBJ-ORIENTED PROG & DESIGN",'location':'OED 112, DCH 1046','description':'''
Discover how stat-of-the-art object-orient programming and design techniques can create globe-spanning software systems that are both flexible and scalable. Learn how software design patterns are used in multiple programming paradigms. Explore highly decoupled systems with dynamically configurable behaviors. Highly recommended for anyone interested in building large systems and software engineering. Basic proficiency in Java is required. Students may not receive credit for both COMP 310/510 and COMP 404/504.
'''},
{'subject':'COMP','number':'556',"title":"INTRO TO COMPUTER NETWORKS",'location':'DCH 1064','description':'''
Network architectures, algorithms, and protocols. Local- and Wide-area networking. Intra- and inter-domain routing. Transmission reliability. Flow and congestion control. TCP/IP. Multicast. Quality of Service. Network Security - Networked applications. Additional coursework required beyond the undergraduate course requirements.
'''},
{'subject':'COMP','number':'431',"title":"WEB DEVELOPMENT",'location':'DCH Sym II Lab','description':'''
In this project-based course, students create multi-user Web applications involving all aspects of application development from front-end and back-end programming to interfacing client-server communications technologies. Class time includes discussions of topics in Web development, structural frameworks, test driven development, and time for students to develop their Web applications.
'''},
{'subject':'COMP','number':'425',"title":"COMPUTER SYSTEMS ARCHITECTURE",'location':'DCH 1070, DCH 1064','description':'''
Evolution of key architecture concepts found in advanced uniprocessor systems. Fundamental and advanced pipelining techniques and associated issues for improving processor performance. Illustrated with RISC processors such as the ARM processor. Examine several metrics for processor performance, such as Amdahl law. Key concepts of data and program memory systems found in modern systems with memory hierarchies and cashes. Perform experiments in cache performance analysis. Influence of technology trends, such as Moore law, on processor implementation Approaches for exploiting instruction level parallelism, such as VLIW. Introduction to parallel and multicore architectures. Introduction to processor architectures targeted for imbedded applications.
'''},
{'subject':'COMP','number':'557',"title":"ARTIFICIAL INTELLIGENCE",'location':'DCH 1064','description':'''
This is a foundational course in artificial intelligence, the discipline of designing intelligent agents. The course will cover the design and analysis of agents that do the right thing in the face of limited information and computational resources. The course revolves around two main questions: how agents decide what to do, and how they learn from experience. Tools from computer science, probability theory, and game theory will be used. Interesting examples of intelligent agents will be covered, including poker playing programs, bots for various games (e.g. WoW), DS1 -- the spacecraft that performed an autonomous flyby of Comet Borrely in 2001, Stanley -- the Stanford robot car that won the Darpa Grand Challenge, Google Maps and how it calculates driving directions, face and handwriting recognizers, Fedex package delivery planners, airline fare prediction sites, and fraud detectors in financial transactions. Additional coursework required beyond the undergraduate course requ
 irements.
'''},
{'subject':'COMP','number':'560',"title":"COMPUTER GRAPHICS",'location':'DCH 1075','description':'''
A survey of core topics in Computer Graphics and Geometric Modeling, including fractals, ray tracing, hidden surface Algorithmic, Bezier, B-spline, blossoming techniques and subdivision procedures.
'''},
{'subject':'COMP','number':'524',"title":"MOBILE AND WIRELESS NETWORKING",'location':'DCH 1075','description':'''
Study of network protocols for mobile and wireless networking, particularly at the media access control, network, and transport protocol layers. Focus is on the unique problems and challenges presented by the properties of wireless transmission and host or router mobility.
'''},
{'subject':'COMP','number':'160',"title":"INTRO TO GAME PROG IN PYTHON",'location':'DCH Sym II Lab','description':'''
This class covers the basics of Python Programming with a focus on building simple games in a web-based environment. The class includes an introduction to event-driven programming and trains the students in the specifics of a Python GUI system designed to support creating to support creating applications that run in a web browser. This course is limited to first-year students only. Continuing Students may register with an approved Special Registration Form.
'''},
{'subject':'COMP','number':'382',"title":"REASONING ABOUT ALGORITHMS",'location':'HRZ 210','description':'''
Writing algorithms is fun, but how are you sure that the algorithm you wrote is flawless? Are there computing tasks for which it is impossible to produce an efficient algorithm, or, for that matter, any algorithm? To answer these questions, you have to learn to perform mathematical reasoning about algorithmic problems and solutions COMP 382 is an introduction to such reasoning techniques. Topics covered would include elementary logic, analysis of the correctness and efficiency of algorithms, and formal computational models like finite automata and Turning machines. On the way, you are also going to learn some new algorithm design techniques.
'''},
{'subject':'COMP','number':'440',"title":"ARTIFICIAL INTELLIGENCE",'location':'DCH 1064','description':'''
This is a foundational course in artificial intelligence, the discipline of designing intelligent agents. The course will cover the design and analysis of agents that do the right thing in the face of limited information and computational resources. The course revolves around two main questions: how agents decide what to do, and how they learn from experience. Tools from computer science, probability theory, and game theory will be used. Interesting examples of intelligent agents will be covered, including poker playing programs, bots for various games (e.g. WoW), DS1 -- the spacecraft that performed an autonomous flyby of Comet Borrely in 2001, Stanley -- the Stanford robot car that won the Darpa Grand Challenge, Google Maps and how it calculates driving directions, face and handwriting recognizers, Fedex package delivery planners, airline fare prediction sites, and fraud detectors in financial transactions.
'''},
{'subject':'COMP','number':'446',"title":"MOBILE DEVICE APPLICATIONS",'location':'DCH 1046','description':'''
As connected smartphones and tablets such as the iPhone and iPad become more popular, updated programming models and design concepts are required to take advantage of their capabilities. COMP/ELEC 446 will consider programming models including natively running applications, web services and mobile tailored web pages. We will explore applications primarily on the Apple iPhone, iPod and iPad but will briefly cover Google Android and Microsoft Windows Phone. We will also briefly touch on the development of web services to support mobile applications. The course culminates with a large project taking up most of the second half of the semester. Curriculum centers around and teaches iOS and code (iPhone/iPad); however final projects may also be completed in any major mobile system if the student has a foundation in Eclipse (Android) or Visual Studio (WP).
'''},
{'subject':'COMP','number':'602',"title":"NEURAL MACHINE LEARNING II",'location':'KCK 107','description':'''
Advanced topics in ANN theories, with a focus on learning high-dimensional complex manifolds with neural maps (Self-Organizing Maps, Learning Vector Quantizers and variants). Application to data mining, clustering, classification, dimension reduction, sparse representation. The course will be a mix of lectures and seminar discussions with active student participation, based on most recent research publications. Students will have access to professional software environment to implement theories.
'''},
{'subject':'COMP','number':'310',"title":"ADV OBJECT-ORIENTED PROG",'location':'HRZ 212, OED 112','description':'''
Discover how state-of-the-art object-orient programming and design techniques can create globe-spanning software systems that are both flexible and scalable. Learn how software design patterns are used in multiple programming paradigms. Explore highly decoupled systems with dynamically configurable behaviors. Highly recommended for anyone interested in building large systems and software engineering.
'''},
{'subject':'COMP','number':'310',"title":"ADV OBJECT-ORIENTED PROG",'location':'HRZ 212, OED 112','description':'''
Discover how state-of-the-art object-orient programming and design techniques can create globe-spanning software systems that are both flexible and scalable. Learn how software design patterns are used in multiple programming paradigms. Explore highly decoupled systems with dynamically configurable behaviors. Highly recommended for anyone interested in building large systems and software engineering.
'''},
{'subject':'COMP','number':'215',"title":"INTRODUCTION TO PROGRAM DESIGN",'location':'BRK 101','description':'''
This course covers the principles of programming and program design. The course is organized around a number of individual programming assignments that fit together to complete a significant, real-world application. Each assignment emphasizes one or more of the basic principles of software design, including: encapsulation, abstraction, test-driven development, and functional and object-oriented programming. The Java programming language will be used. An introduction to the basics of the Java language itself (including Java syntax and semantics) will be provided.
'''},
{'subject':'COMP','number':'485',"title":"FUND MEDICAL IMAGING I",'location':'BRC 284','description':'''
This course will introduce basic principles of image acquisition, formation and processing of several medical imaging modalities such as X-Ray, CT, MRI, and US that are used to evaluate the human anatomy. The course also includes visits to a clinical site to gain experience with the various imaging modalities covered in class.
'''},
{'subject':'COMP','number':'429',"title":"INTRO TO COMPUTER NETWORKS",'location':'DCH 1064','description':'''
Network architectures, algorithms, and protocols. Local- and Wide-area networking. Intra- and inter-domain routing. Transmission reliability. Flow and congestion control. TCP/IP. Multicast. Quality of Service. Network Security - Networked applications.
'''},
{'subject':'COMP','number':'413',"title":"DISTRIB PROGRAM CONSTRUCTION",'location':'DCH 1075','description':'''
This course focuses on modern principles for the construction of distributed programs, with an emphasis on design patterns, modern programming tools, and distributed object systems. The material will be applied in a substantial software design/construction project.
'''},
{'subject':'COMP','number':'326',"title":"DIGITAL LOGIC DESIGN",'location':'DCH 1070','description':'''
Study of gates, flip-flops, combinational and sequential switching circuits, registers, logical and arithmetic operations, introduction to the Verilog hardware description language.
'''},
{'subject':'COMP','number':'522',"title":"MULTI-CORE COMPUTING",'location':'DCH 1075','description':'''
Multi-core microprocessors are becoming the norm. The course will focus on emerging multi-core processor architectures and challenges to using them effectively. Topics include multi-core microcompressors, memory hierarchy, synchronization, programming systems, scheduling, and transactional memory.
'''},
{'subject':'COMP','number':'360',"title":"COMPUTER GRAPHICS",'location':'DCH 1075','description':'''
2D graphics techniques including fast line and curve drawing and polygon filling. 3D graphics problems including representation of solids, shading, and hidden surface elimination. Fractals, graphics standards.
'''},
{'subject':'COMP','number':'693',"title":"ADV TOPICS - COMPUTER SYSTEMS",'location':'DCH 3110','description':'''
This course is a discussion based seminar about state of the art embedded and digital signal processing systems, with emphasis on both hardware architectures as well as software tools, programming models, and compilers. The seminar focuses on state of the art academic and commercial offerings in these areas.
'''},
{'subject':'COMP','number':'162',"title":"INTRO TO GAME CONTENT CREATION",'location':'DCH Sym II Lab','description':'''
Explore how modern game content is created, and how it interacts with the underlying technology. Beginning with an explanation of how games are developed and what role content plays in the process, the class will learn to use 3D Studio Max, Photoshop, and game-native scripting as they create working content for an established game project.
'''},
{'subject':'COMP','number':'600',"title":"GRADUATE SEMINAR",'location':'DCH 1070','description':'''
This seminar course meets weekly to discuss current research results by graduate students in the Computer Science Department. Senior students are expected to present their results.
'''},
{'subject':'COMP','number':'100',"title":"INTRO COMPUTING & INFO SYS",'location':'DCH Sym II Lab','description':'''
An introduction to organizing, analyzing, and presenting information using databases and spreadsheets. No programming involved, and no computing background expected.SP 2016, Section 001: Class will be taught by Mackale Joyner.
'''},
{'subject':'HIST','number':'387',"title":"U.S. & THE WORLD: 1750-1900",'location':'HUM 327','description':'''
This course provides an overview of the United States鈥?interactions with the world from the revolutionary period to the Spanish-American war. Impact of international affairs on the evolution of U.S. domestic institutions, changing ideas about America鈥檚 role in the world by key political figures, private-sector activists, intellectuals, and citizens at large.
'''},
{'subject':'MGMT','number':'659',"title":"REAL ESTATE FINANCE",'location':'MCN 312','description':'''
This course provides an introduction to the concepts and techniques used to analyze and commercial real estate assets and the instruments commonly used to finance these assets. The topics covered include financial analysis of income-generating real property, analysis of mortgage instruments, commercial mortgage-backed securities (CMBS), and real estate investment trusts (REITs). This course is designed for students who are interested in commercial real estate; topics pertaining to single-family residential real estate will be covered only in passing. The course will offer all students an opportunity to develop their business presentation skills through case discussions and a final project presentation. The final project involves the detailed analysis of a CMBS deal, including separate, linked analyses of the mortgage collateral pool, the mortgages, and the note structure. The final project will require the use of all of the tools developed in the course.
'''},
{'subject':'MECH','number':'435',"title":"INTRO TO MECHATRONICS",'location':'MEB 128','description':'''
Introduction to electromechanical systems, focusing on motor mechanics, electric drives & electronics, & modern digital control algorithms. Covers basic principles of electromechanical energy conversion & motor control. Students are introduced to energy efficiency considerations of modern electric drives. Includes hands-on laboratory projects involving digital computer control of various motor types.
'''},
{'subject':'ARCH','number':'654',"title":"CINEMAS OF URBAN ALIENATION",'location':'HRG 126','description':'''
This seminar examines cinematic engagements with urban spaces and experiences around the world spanning the last two centuries. Particular attention will be paid to issues of migration, marginality, colonialism, war and post-war, nostalgia and memory, race and gender. Cities of focus include Berlin, Istanbul, Moscow, Algiers, Beirut and Paris. Our weekly discussions of individual films will be grounded in critical writings of the cities' histories and theories of space and film.
'''}
]
        img_set = [
{'location':'DCH','imgsrc':'https://s9.postimg.org/56ckls6gv/Duncan_Hall.jpg'},
{'location':'MCH','imgsrc':'https://s4.postimg.org/d6ssl3tjx/mcnair_hall.jpg'},
{'location':'HUM','imgsrc':'https://s12.postimg.org/68t84k2zx/humanities.jpg'},
{'location':'MEB','imgsrc':'https://s18.postimg.org/z3mhe6cc9/meb.jpg'},
{'location':'HRG','imgsrc':'https://s14.postimg.org/x0dmkpmhd/robert.jpg'}
]
        all_course_pre =  self.db.table('course_data_1').all()
        for course in all_course_pre:
            self.db.table('course_data_1').delete(course.get('id'))
        for course in course_data:
            self.db.table('course_data_1').add(course)
        img_pre =  self.db.table('img_data_1').all()
        for img in img_set:
            self.db.table('img_data_1').delete(img.get('id'))
        for img in img_set:
            self.db.table('img_data_1').add(img)
        message = self.create_message(text="Hi, glad to meet you!")
        return self.respond(message= message, action="next")