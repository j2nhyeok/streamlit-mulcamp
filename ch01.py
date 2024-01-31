import streamlit as st
import streamlit.components.v1 as components
from datetime import datetime
import pytz
import pandas as pd
import numpy as np
import altair as alt
def main():
    animal_shelter = ['cat', 'dog', 'rabbit', 'bird']

    animal = st.text_input('Type an animal')

    if st.button('Check availability'):
        have_it = animal.lower() in animal_shelter
        'We have that animal!' if have_it else 'We don\'t have that animal.'
        
    st.write(datetime(2020, 1, 10, 10, 30, tzinfo=pytz.timezone("EST")))
    st.title("안녕하세요!!")
    st.header("This is Header")
    st.subheader("이거슨 subheader")
    st.write("파이썬 문법 사용 가능")
    st.write("-"*50)

    st.markdown("HTML JS Streamlit 적용")
    js_code = """ 
       <h3>Hi</h3>
       <script>
       function sayHello() {
           alert('Hello from JavaScript in Streamlit Web');
       }
       </script>
       <button onclick="sayHello()">Click me</button>
       """
    components.html(js_code)

    '''
    # This is the document title

    This is some _markdown_.
    '''

    import pandas as pd
    df = pd.DataFrame({'col1': [1, 2, 3]})
    df  # 👈 Draw the dataframe

    x = 10
    'x', x  # 👈 Draw the string 'x' and then the value of x

    # Also works with most supported chart types
    import matplotlib.pyplot as plt
    import numpy as np

    arr = np.random.normal(1, 1, size=100)
    fig, ax = plt.subplots()
    ax.hist(arr, bins=20)

    fig  # 👈 Draw a Matplotlib chart

    st.write("-" * 50)
    a = 1
    b = 2
    st.write(a+b)
    st.write("-" * 50)

    st.markdown("*Streamlit* is **really** ***cool***.")
    st.markdown('''
        :red[Streamlit] :orange[can] :green[write] :blue[text] :violet[in]
        :gray[pretty] :rainbow[colors].''')
    st.markdown("Here's a bouquet &mdash;\
                :tulip::cherry_blossom::rose::hibiscus::sunflower::blossom:")

    multi = '''If you end a line with two spaces,
    a soft return is used for the next line.

    Two (or more) newline characters in a row will result in a hard return.
    '''
    st.markdown(multi)


    st.caption('This is a string that explains something above.')
    st.caption('A caption with _italics_ :blue[colors] and emojis :sunglasses:')

    code = '''def hello():
        print("Hello, Streamlit!")'''
    st.code(code, language='python')

    st.text('This is some text.')

    st.latex(r'''
    a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
    \sum_{k=0}^{n-1} ar^k =
    a \left(\frac{1-r^{n}}{1-r}\right)
    ''')

    st.write("This is some text.")

    st.slider("This is a slider", 0, 100, (25, 75))

    st.divider()  # 👈 Draws a horizontal rule

    st.write("This text is between the horizontal rules.")

    st.divider()  # 👈 Another horizontal rule

    df = pd.DataFrame(np.random.randn(50, 20), columns=("col %d" % i for i in range(20)))

    st.dataframe(df)  # Same as st.write(df)

    st.write("-" * 50)
    chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])

    st.scatter_chart(chart_data)

    chart_data = pd.DataFrame(np.random.randn(200, 3), columns=["a", "b", "c"])

    st.vega_lite_chart(
        chart_data,
        {
            "mark": {"type": "circle", "tooltip": True},
            "encoding": {
                "x": {"field": "a", "type": "quantitative"},
                "y": {"field": "b", "type": "quantitative"},
                "size": {"field": "c", "type": "quantitative"},
                "color": {"field": "c", "type": "quantitative"},
            },
        },
    )

    arr = np.random.normal(1, 1, size=100)
    fig, ax = plt.subplots()
    ax.hist(arr, bins=20)

    st.pyplot(fig)

if __name__ == "__main__":
    main()