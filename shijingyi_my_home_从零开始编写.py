'''我的主页'''
import streamlit as st
# from streamlit_drawable_canvas import st_canvas
from PIL import Image


page = st.sidebar.radio('我的首页', ['兴趣推荐', '图片处理', '我的智能词典', '我的留言区'])

def page_1():
    '''兴趣推荐'''
    with open('DJ OKAWARI - Flower Dance.ogg','rb') as f:
        mymp3 = f.read()
    st.audio(mymp3,format='audio0/mp3',start_time=0)
    st.write('我的音乐')
    st.write('------------------------------')
    st.write('我的电影')
    st.write('------------------------------')
    st.write('我的美食')
    st.write('------------------------------')
    st.write('我的书籍')
    st.write('------------------------------')

def page_2():
    '''我的图片处理工具'''
    st.write(":sunglasses:图片处理:sunglasses")
    uploaded_file=st.file_uploader("上传图片",type=['png','jpeg','jpg'])
    if uploaded_file:
        file_name=uploaded_file.name
        file_type=uploaded_file.type
        file_size=uploaded_file.size
        img=Image.open(uploaded_file)
        st.image(img)
        st.image(img_change(img))
    def img_change(img):
        '''图片处理'''
        width,height=img.size
        image_array=img.load
        for x in range(width):
            for y in range(height):
                #获取RGB值
                r=image_array[x.y][0]
                g=image_array[x.y][1]
                b=image_array[x.y][2]
                image_array[x,y]=(b,g,r)
        return img

def page_3():
    '''我的智能词典'''
    st.write('我的智能词典')
    with open('words_space1.txt','r',encoding='utf-8') as f:
        words_list=f.read().split('\n')
    for i in range(len(words_list)):
         words_list[i]=words_list[i].split('#')
    words_dict={}
    for i in words_list:
        words_dict[i[1]]=[int(i[0]),i[2]]
    
    with open('check_out_times.txt','r',encoding='utf-8') as f:
        times_list=f.read().split('\n')
    for i in range(len(times_list)):
         times_list[i]=times_list[i].split('#')
    times_dict={}
    
    for i in times_list:
        times_dict[int(i[0])]=[int(i[1])]
    word=st.text_input('请输入要查询的单词')
    if word in words_dict:
        st.write(words_dict[word])
        n=words_dict[word[0]]
        if n in times_dict:
            times_dict[n]+=1
        else:
            times_dict[n]=1
        with open('check_out_times.txt','w',encoding='utf-8') as f:
            message=''
            for k,v in times_dict.items():
                message += str(k)+'#'+str(v)+'\n'
                message=message[:-1]
                f.write(message)
            st.write('查询次数：',times_dict[n])
    
def page_4():
    '''我的留言区'''
    st.write('我的留言区')
    with open('leave_messages.txt','r',encoding='utf-8') as f:
        messages_list=f.read().split()
    for i in range(len(messages_list)):
        messages_list[i]=messages_list[i].split('#')
    # for i in messages_list:
    #     if i[1]=='魏卓菲':
    #         with  st.chat_message('')
    #         st.write(i[1],':',i[2])
    #     elif i[1]=='胡语辰':
    #         with st.chat_message(''):
    #             st.write(i[1],':',i[2])
    # name=st.selectbox(' 我是_',['魏卓菲','胡语辰'])
    # new_message=st.text_input('想要说的话...')
    # if st.button('留言')
    # messages_list.append(str(int(messages_list[-1][0]+1)),name,new_message)
        
if page == '我的智能词典':
    page_3()
elif page == '我的留言区':
    page_4()
