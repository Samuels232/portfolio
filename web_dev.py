import streamlit as st
from streamlit_js_eval import streamlit_js_eval

st.set_page_config(layout="wide")
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
st.markdown(
    """
    <nav>
        <div class="nav-left"><span class="col">S</span>ammy's🥑</div>
        <div class="nav-right">
            <a href="#" class="fit">Home</a>
            <a href="#" class="fit">About</a>
            <a href="#" class="fit">Portfolio</a>
            <a href="#" class="fit">Contact</a>
        </div>
    </nav>
    <style>
        nav{
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 5%;
            background: linear-gradient(to bottom right, #2C003E, #000000);
            padding: 0px 5px;
            position: fixed;
            top: 3.5rem;
            left: 0;
            width: 100%;
            z-index: 9999;
            z-index: 100%;
            box-shadow: 0 2px 6px rgba(0,0,0,0.5);
        }
        .nav-left{
            font-size: 30px;
        }
        .col{
            font-style: bold;
            font-weight: 700;
            font-size: 40px;
            color: grey;
        }
        .nav-right{
            margin-right: 10px;
        }
        .nav-right a{
            height: 100%;
            text-decoration: none;
            margin-left: 10px;
            margin-top: 0px;
            color: grey;
            padding: 8px;
            font-size: 20px;
            font-weight: 500;
        }
        .nav-right a:hover{
            color: white;
            background: grey;
            box-shadow: 0 0 7px black;
        }
    """, unsafe_allow_html=True
)
after_nav = st.container()
with after_nav:
    col1, col2 = st.columns([4,6])
    with col1:
        st.image("images/prof.jpg")
    with col2:
        st.markdown("""
            <div class="bout-left">
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
            <div class="ab-left"><img src="http://raw.githubusercontent.com/Samuels232/portfolio/main/images/peak1.jpg"></img></div>
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
        <div class="portfolio">
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
    st.markdown("""
        <div class="Talk">
            <div class="talk-left">
                <div class="socials"><img src="http://raw.githubusercontent.com/Samuels232/portfolio/main/images/git1.jpg"></div>
                <div class="socials"><img src="http://raw.githubusercontent.com/Samuels232/portfolio/main/images/wat1.png"></div>
                <div class="socials"><img src="http://raw.githubusercontent.com/Samuels232/portfolio/main/images/ig.jpg"></div>
                <div class="socials"><img src="http://raw.githubusercontent.com/Samuels232/portfolio/main/images/snap.jpg"></div>
            </div>
            <div class="talk-right">
                <form id="contactForm">
                    <input type="text" id="name" placeholder="Your name" required>
                    <textarea id="message" placeholder="Your message" required>
                    <button type="submit">Submit</button>
                </form>
            </div>
        </div>
        
        <style>
            .Talk{
                display: flex;
            }
            .talk-left{
                flex-basis: 20%
            }
            .socials{
                margin: 5px;
            }
            .socials img{
                width: 70px;
                height: 70px;
            }
        </style>
    """,unsafe_allow_html=True)