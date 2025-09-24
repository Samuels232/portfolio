import streamlit as st

st.set_page_config(layout="wide")
st.markdown(
    """
    <nav>
        <div class="nav-left"><span class="col">S</span>ammy's🥑</div>
        <div class="nav-right">
            <a href="#about" class="fit fi">Home</a>
            <a href="#" class="fit">Portfolio</a>
            <a href="#" class="fit">Contact</a>
        </div>
    </nav>
    <style>
        nav{
            display: flex;
            justify-content: space-between;
            width: 100%;
            align-items: center;
            margin-bottom: 5%;
            background: linear-gradient(to bottom right, #2C003E, #000000);
            padding: 0px 5px;
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
            background: green;
            box-shadow: grey;
        }
        .nav-right a:first-child:hover{
            border-radius: 15px 0 0 0;
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
            <div class="ab-left"><img src="images/peak.jpg"></img></div>
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
                <div class="ab">
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
            }
            .ab-left{
                display: flex;
                flex-basis: 40%;
                border-radius: 15px;
            }
            .ab-left img{
                width: 100%;
                border: 1px solid;
                border-radius: inherit;
            }
            .ab-middle{
                display: flex;
                flex-basis: 5%;
            }
            .ab-right{
                display: flex;
                flex-direction: column;
                flex-basis: 55%;
                linear-gradient: linear-gradient(to right, rgb(76, 76, 80), rgb(145, 139, 139));
            }
            .ab{
                background: linear-gradient(to bottom right, #2C003E, #000000);
                border-radius: 12px;
                padding: 0 15px;
                margin: 30px 0 0 0;
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
                font-size: 18px;
                font-style: Verdana;
            }
            @media (max-width: 1024px) and (min-width: 360px){
                .about-cuz{
                    display: flex;
                    flex-direction: column;
                    height: 1300px;
                }
                .ab-left{
                    display: flex;
                    flex-basis: 55%;
                    border: 1px solid;
                    border-radius: 15px;
                }
                .ab-left img{
                    height: 100%;
                    border: 1px solid;
                    width: inherit;
                    border: inherit;
                    border-radius: inherit;
                }
                .ab-right{
                    display: flex;
                    flex-basis: 40%;
                }
                
            }
        </style>
    """,unsafe_allow_html=True)