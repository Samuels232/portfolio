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
            background: linear-gradient(to right, rgb(76, 76, 80), rgb(145, 139, 139));
            padding: 0px 5px;
        }
        .nav-left{
            font-size: 30px;
        }
        .col{
            font-style: bold;
            font-weight: 700;
            font-size: 40px;
            color: green;
        }
        .nav-right{
            margin-right: 10px;
        }
        .nav-right a{
            height: 100%;
            text-decoration: none;
            margin-left: 10px;
            margin-top: 0px;
            color: green;
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
                    background: linear-gradient(to right, rgb(76, 76, 80), rgb(145, 139, 139));
                }
            </style>
        """,unsafe_allow_html=True)
        for i in range(4):
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
                    <style>
                        .bout-lef{
                            font-size: 25px;
                            background: linear-gradient(to right, rgb(76, 76, 80), rgb(145, 139, 139));
                            padding: 20px 10px 15px 10px;
                            border-radius: 15px;
                            box-shadow: -5px 5px 7px rgb(15, 15, 15);
                            transition: 0.5s;
                            cursor: pointer;
                            transition: 500ms;
                        }
                        .bout-lef p{
                            display: inline;
                        }
                        
                        .bout-lef:hover{
                            background: linear-gradient(to right, rgb(76, 76, 80), rgb(145, 139, 139));
                        }
                    </style>
                """, unsafe_allow_html=True)

