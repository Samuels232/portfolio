import streamlit as st
import send_email as em

st.set_page_config(layout="wide")
st.markdown("""
    <style>
        #MainMenu {visibility: hidden;}
        header {visibility: hidden;}
        footer {visibility: hidden;}
    </style>
""",unsafe_allow_html=True)
st.markdown("""
    <style>
        *{
            scroll-behavior: smooth !important;
        }
    </style>
""",unsafe_allow_html=True)
st.markdown("""
    <style>
        :root{
            color-scheme: only dark;
        }
        body{
            background-color: #0d0d0d !important;
            color: #f1f1f1; !important;
        }
    </style>
""",unsafe_allow_html=True)
st.markdown("""
    <div class="desktop-nav">
        <div class="navleft">Sammy's🥑</div>
        <div class="navright">
            <a href="#homie">Home</a>
            <a href="#about">About</a>
            <a href="#portfolio">Portfolio</a>
            <a href="#contact">Contact</a>
       </div>
    </div>

    <div class="mobile-nav">
      <!-- Toggle (checkbox + label for hamburger) -->
      <input type="checkbox" id="nav-toggle" class="nav-toggle">
      <label for="nav-toggle" class="hamburger">&#9776;</label>
    
      <div class="navleft">Sammy's🥑</div>
      
      <label for="nav-toggle" class="nav-overlay"></label>
    
      <div class="nav-menu">
        <a href="#homie">Home</a>
        <a href="#about">About</a>
        <a href="#portfolio">Portfolio</a>
        <a href="#contact">Contact</a>
      </div>
    </div>

    <style>
        /* General reset */
        body {
          margin: 0;
          font-family: Arial, sans-serif;
          scroll-behavior: smooth; /* smooth scroll globally */
        }
        
        /* Desktop nav */
        .desktop-nav {
          display: flex;
          justify-content: space-between;
          align-items: center;
          padding: 15px 30px;
          background: linear-gradient(to right, #2C003E, #000000);
          color: white;
          position: fixed;
          top: 0;
          left: 0;
          width: 100%;
          z-index: 999;
        }
        
        .desktop-nav .navleft {
          font-size: 22px;
          font-weight: bold;
        }
        
        .desktop-nav .navright {
          display: flex;
          gap: 25px;
        }
        
        .desktop-nav .navright a {
          text-decoration: none;
          color: white;
          font-size: 16px;
          transition: color 0.3s ease;
        }
        
        .desktop-nav .navright a:hover {
          color: #FFD43B; /* Python yellow for hover */
        }
        
        /* Mobile nav hidden by default */
        .mobile-nav {
          display: none;
        }
        
        /* Mobile nav styling */
        @media (max-width: 768px) {
          .desktop-nav {
            display: none; /* hide desktop nav */
          }
        
          .mobile-nav {
            display: block;
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            background: linear-gradient(to right, #2C003E, #000000);
            color: white;
            padding: 10px;
            z-index: 1000;
          }
        
          /* Hide nav menu by default */
          .nav-menu {
            display: none;
            flex-direction: column;
            gap: 15px;
            margin-top: 50px;
            position: fixed;
            top: 0;
            left: 0;
            height: 100vh;
            width: 70%;
            background: linear-gradient(to bottom, #2C003E, #000000);
            padding: 20px 20px 20px 15px;
            z-index: 1001;
          }
        
          /* Toggle button (hamburger) */
          .hamburger {
            font-size: 28px;
            cursor: pointer;
            user-select: none;
            z-index: 1002;
            position: relative;
          }
        
          /* Hide actual checkbox */
          .nav-toggle {
            display: none;
          }
        
          /* Overlay for closing */
          .nav-overlay {
            display: none;
          }
        
          .nav-toggle:checked ~ .nav-overlay {
            display: block;
            position: fixed;
            top: 0;
            left: 0;
            width: 100vw;
            height: 100vh;
            background: rgba(0,0,0,0.6);
            z-index: 1000;
          }
        
          /* Show menu when checked */
          .nav-toggle:checked ~ .nav-menu {
            display: flex;
          }
        
          /* Links */
          .nav-menu a {
            text-decoration: none;
            color: white;
            font-size: 18px;
          }
        
          .nav-menu a:hover {
            text-decoration: underline;
            color: #FFD43B;
          }
        
          .mobile-nav .navleft {
            font-size: 20px;
            font-weight: bold;
            margin-left: 0px;
          }
        }
    </style>
""", unsafe_allow_html=True)

after_nav = st.container()
with after_nav:
    col1, col2 = st.columns([4,6])
    with col1:
        st.image("images/prof.jpg")
    with col2:
        st.markdown("""
            <div id="homie" class="bout-left">
                <p>
                    <h1>Hi,</h1> I'm Sammy, computer science student<br>Having great Interest in AI research and Web-Development.
                </p>
            </div>
            <style>
                .bout-left{
                    font-size: 25px;
                    backdrop-filter: blur(30px);
                    padding: 20px 10px 15px 10px;
                    border-radius: 15px;
                    box-shadow: -5px 5px 7px rgb(15, 15, 15);
                    transition: 0.5s;
                    cursor: pointer;
                    transition: 500ms;
                }
                .bout-left p{
                    display: inline;
                }
                
                .bout-left:hover{
                    transform: translateY(20px);
                    background: linear-gradient(to left, rgb(76, 76, 80), rgb(145, 139, 139));
                }
            </style>
        """,unsafe_allow_html=True)
        for i in range(2):
            st.write("")
            i+=1
        st.markdown("""
                    <div class="bout-lef">
                        <p>
                            A curious mind walking the thin line between AI research and web development. Still
                            learning, still sharpening my craft-but with every line of code, I'm engeneering tools that
                             touch lives. I'm not just chasing trends; I'm devoted to building what last.
                        </p>
                    </div>
                    <div class="bout-lef bout-second">
                        <p>
                            A curious mind walking the thin line between AI research and web development. I'm not just chasing trends; I'm devoted to building what last.
                        </p>
                    </div>
                    <style>
                        .bout-lef{
                            font-size: 25px;
                            background: linear-gradient(to right, rgb(76, 76, 80), rgb(145, 139, 139));
                            padding: 20px 10px 15px 10px;
                            border-radius: 15px 0 0 0;
                            box-shadow: -5px 5px 7px rgb(15, 15, 15);
                            transition: 0.5s;
                            cursor: pointer;
                            transition: 500ms;
                        }
                        .bout-lef p{
                            display: inline;
                        }
                        .bout-second{
                            display: none;
                        }
                        .bout-lef:hover{
                            background: linear-gradient(to right, rgb(76, 76, 80), rgb(145, 139, 139));
                        }
                        @media(max-width: 1023px) and (min-width: 768px){
                            .bout-lef{
                                display: none;
                            }
                            .bout-second{
                                display: block;
                            }
                        }
                        
                    </style>
                """, unsafe_allow_html=True)

top = st.container()
with top:
    for i in range(3):
        st.write("")
        i+=1
    st.title("About Me")
    st.markdown("""
        <div class="about-cuz">
            <div id="about" class="ab-left"><img src="http://raw.githubusercontent.com/Samuels232/portfolio/main/images/peak1.jpg"></img></div>
            <div class="ab-middle">
            </div>
            <div class="ab-right">
                <div class="ab">
                    <h2>Who Am I</h2>
                    <p>I'm a young developer walking the thin line between curiosity and mastery. Still evolving,
                    still learning, but already leaving footprints in code. I don't just write programs-I create
                    experiences that linger. Wherever I step in, I strive to bring clarity, structure and undeniable value
                    </p>
                </div>
                <div class="ab ab-m">
                    <h2>What I Do</h2>
                    <p>I explore the edges of AI and web development, blending logic with creativity to build solutions
                     that actually matter. from functional we apps to experimental AI projects, I thrive on making ideas
                      tangible-shaping concept into tools people can touch, use and rely on. I may be lerning but every
                       line of code is write with intent.</p>
                </div>
                <div class="ab">
                    <h2>What Drives Me</h2>
                    <p>Code, for me, isn't just syntax;<br>
                    it's a language to change lives and upgrade what already exists. My drive is simple: take whats 
                    broken and make it better, take whats ordinary and push it further. I believe in progress that speaks 
                    for itself-the kind you don't see coming until its a;ready shifted the ground beneath you.
                </div>
            </div>
        </div>
        <style>
            .about-cuz{
                display: flex;
                gap: 20px;
            }
            .ab-left{
                flex-basis: 40%;
                position: relative;
                width: 100%;
                height: auto;
                border-radius: 15px;
                overflow: hidden;
                box-shadow: 0 6px 25px rgba(75,0,130,0.7);
            }
            .ab-left::after{
                content: "";
                position: absolute;
                inset: 0;
                border-radius: 15px;
                background: linear-gradient(to bottom right, rgba(44,0,62,0.6),rgba(255,255,255,0.1),rgba(44,0,62,0.7));
            }
            .ab-left img{
                width: 100%;
                height: 100%;
                object-fit: cover;
                display: block;
                border-radius: 15px;
            }
            
            .ab-middle{
                display: flex;
                flex-basis: 5%;
            }
            .ab-right{
                display: flex;
                flex-direction: column;
                flex-basis: 55%;
                linear-gradient: linear-gradient(to bottom right, #2C003E, #000000);
            }
            .ab{
                cursor: pointer;
                background: linear-gradient(to bottom right, #2C003E, #000000);
                border-radius: 12px;
                padding: 0 15px;
                margin: 30px 0 0 0;
                box-shadow: 0 8px 30px rgba(88,24,69,0.5);
                transition: all 0.5s;
            }
            .ab:hover{
                transform: scale(1.1);
            }
            .ab h1{
                font-style: Impact;
            }
            .ab p{
                background: linear-gradient(to top right, #3776AB,#FFD43B,#306998,#4B8BBE,#646464,#A9A9A9,#D3D3D3);
                -webkit-background-clip: text;
                -webkit-text-fill-color: transparent;
                background-clip: text;
                color: transparent;
                font-size: 19px;
                font-style: Verdana;
            }
            .ab-m p{
                background: linear-gradient(to top left, #3776AB,#FFD43B,#306998,#4B8BBE,#646464,#A9A9A9,#D3D3D3);
                -webkit-background-clip: text;
                -webkit-text-fill-color: transparent;
                background-clip: text;
                color: transparent;
                font-size: 19px;
                font-style: Verdana;
            }
            @media (max-width: 1024px) and (min-width: 344px){
                .about-cuz{
                    flex-direction: column;
                }
                .ab-left{
                    flex-basis: auto;
                    width: 100%;
                }
                .ab-left img{
                    width: 100%;
                    height: auto;
                }
                
            }
        </style>
    """,unsafe_allow_html=True)

portfolio = st.container()
with portfolio:
    for i in range(3):
        st.write("")
    st.title("Portfolio")
    st.markdown("""
        <div id="portfolio" class="portfolio">
            <div class="work">
                <img src="http://raw.githubusercontent.com/Samuels232/portfolio/main/images/ai1.jpg">
                <div class="layer">
                    <h3>Artificial Intelligence</h3>
                    <p>I build practical AI solutions that merge intelligence with reusability. My goal is to create an 
                    AI that feels less like a tool and more like a collaborator</p>
                </div>
            </div>
            <div class="work">
                <img src="http://raw.githubusercontent.com/Samuels232/portfolio/main/images/webs.png">
                <div class="layer">
                    <h3>Web Development</h3>
                    <p>From front-end design to back-end logic, I build web solutions that balance creativity with 
                    functionality. Every project aims to connect users effortlessly</p>
                </div>
            </div>
            <div class="work">
                <img src="http://raw.githubusercontent.com/Samuels232/portfolio/main/images/uui3.jpg">
                <div class="layer">
                    <h3>UI/UX Design</h3>
                    <p>UI/UX to me is about clarity and flow. I craft designs that not only look good but guide users 
                    seamlessly through every interaction.</p>
                </div>
            </div>
        </div>
        <div class="center-box">
            <a href="https://github.com/Samuels232" class="glow-link">Project Repository</a>
        </div>
        <style>
            .portfolio{
                display: grid;
                grid-template-columns: repeat(auto-fit, minmax(250px,1fr));
                grid-gap: 40px;
                margin-top: 20px;
            }
            .work{
                cursor: pointer;
                border-radius: 10px;
                position: relative;
                overflow: hidden;
            }
            .work img{
                width: 100%;
                border-radius: 10px;
                display: block;
                transition: transform 0.5s;
            }
            .layer{
                width: 100%;
                height: 0;
                background: linear-gradient(to bottom right, rgba(44,0,62,0.6),rgba(255,255,255,0.1),rgba(44,0,62,0.7));
                border-radius: 10px;
                position: absolute;
                left: 0;
                bottom: 0;
                overflow: hidden;
                display: flex;
                flex-direction: column;
                align-items: center;
                justify-content: center;
                padding: 0 40px;
                text-align: center;
                font-size: 14px
            }
            .layer h3{
                font-weight: 500;
                margin-bottom: 20px;
            }
            .work:hover img{
                transform: scale(1.1);
            }
            .work:hover .layer{
                height: 100%;
            }
            .center-box{
                display: flex;
                justify-content: center;
                align-items: center;
                margin-top: 30px;
            }
            .glow-link {
              display: inline-block;
              font-size: 1.2rem;
              font-weight: bold;
              color: #fff !important;
              text-decoration: none !important;
              padding: 10px 20px;
              border-radius: 40px;
              background: linear-gradient(135deg, #2C003E, #000000);
              box-shadow: 0 0 15px #2C003E, 0 0 25px #000000;
              animation: glowing 2s infinite alternate;
              transition: transform 0.3s ease;
            }
            
            .glow-link:hover {
              transform: scale(1.05);
            }
            
            @keyframes glowing {
              0% {
                box-shadow: 0 0 5px #2C003E, 0 0 10px #000000;
              }
              50% {
                box-shadow: 0 0 20px #2C003E, 0 0 40px #000000;
              }
              100% {
                box-shadow: 0 0 10px #2C003E, 0 0 20px #000000;
              }
            }

        </style>
""",unsafe_allow_html=True)

bottom = st.container()
with bottom:
    for i in range(3):
        st.write("")
    st.title("Lets Talk")
    col1, col2 = st.columns([1,2])
    with col1:
        st.markdown("""
            <div id="contact" class="left">
                <div class="talk-left">
                        <br><br>
                        <a href="https://github.com/Samuels232"><img src="http://raw.githubusercontent.com/Samuels232/portfolio/main/images/git1.jpg" width="80px"></a>
                        <a href="https://wa.me/0274708989"><img src="http://raw.githubusercontent.com/Samuels232/portfolio/main/images/wat2.jpg" width="80px"></a> 
                        <a href="https://www.instagram.com/sammyspear28"><img src="http://raw.githubusercontent.com/Samuels232/portfolio/main/images/ig.jpg" width="80px"></a>
                        <a href="https://www.snapchat.com/add/lilcode9885"><img src="http://raw.githubusercontent.com/Samuels232/portfolio/main/images/snap.jpg" width="80px"></a>
                </div>
                <div class="talk-middle" style=""></div>
            </div>
            <style>
                .left{
                display: flex;
                justify-content: space-between;
                align-items: center;              
                }
                .talk-left{
                    display: flex;
                    flex-direction: column;
                }
                .talk-left a{
                    transition: all 0.5s;
                }
                .talk-left a:hover{
                    transform: scale(1.1);
                }
                .talk-left a img{
                    border-radius: 50px;
                    margin: 5px;
                }
                .talk-middle{
                border-left: 2px solid white; 
                height: 400px;
                margin-top: 10%; 
                margin-right: 15%;   
                }
                @media (max-width: 760px) and (min-width: 344px){
                    .left{
                        display: flex;
                    }
                    .talk-left{
                        display: flex;
                        flex-direction: row;
                        margin-left: 5px;
                    }
                    .talk-middle{
                        display: none;
                    }
                }
            </style>    
        """,unsafe_allow_html=True)

    with col2:
        for i in range(1):
            st.write("")
            i+=1
        with st.form("my_form"):
            name = st.text_input("Your name")
            email = st.text_input("Email")
            message = st.text_area(
                "Your message",
                height=200,
                max_chars=500,
                key="feedback_box"
            )
            submitted = st.form_submit_button("Submit")
body = ""
if submitted:
    if name and email and message:
        body = body + name + "\n" + email + "\n" + message
        body = body.encode("Utf-8")
        em.send_email(body)
        st.success(f"Thanks for your feedback, {name}!😊")
    else:
        st.error("Please fill in all fields before submitting.")

