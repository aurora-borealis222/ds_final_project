import streamlit as st
import matplotlib.pyplot as plt
import mpld3
import streamlit.components.v1 as components
from PIL import Image

from data import get_salaries, get_inflation, get_salaries_real, get_inflation_influence

st.set_page_config(
    page_title='Анализ данных о заработных платах',
    layout='wide'
)

st.header('Среднемесячная номинальная заработная плата по трем видам экономической деятельности за 2000-2023 гг.', anchor='salaries')

df_salaries = get_salaries()
st.dataframe(df_salaries)

st.write('Построим графики изменения номинальной заработной платы (НЗП) по годам для этих видов экономической деятельности (графики интерактивны):')

years = df_salaries['year']

construction = df_salaries['construction']
fig = plt.figure()
plt.plot(years, construction, marker='o')
plt.title('Строительство')
plt.xlabel('Год')
plt.ylabel('НЗП, рублей')

fig_html = mpld3.fig_to_html(fig)
components.html(fig_html, height=600)


education = df_salaries['education']
fig = plt.figure()
plt.plot(years, education, marker='o')
plt.title('Образование')
plt.xlabel('Год')
plt.ylabel('НЗП, рублей')

fig_html = mpld3.fig_to_html(fig)
components.html(fig_html, height=600)


healthcare_social_services = df_salaries['healthcare_social_services']
fig = plt.figure()
plt.plot(years, healthcare_social_services, marker='o')
plt.title('Здравоохранение и социальные услуги')
plt.xlabel('Год')
plt.ylabel('НЗП, рублей')

fig_html = mpld3.fig_to_html(fig)
components.html(fig_html, height=600)


st.write('Также построим объединенный график для всех трех видов экономической деятельности:')

fig = plt.figure(figsize=(10, 5))

plt.plot(years, construction, marker='o', label='Строительство')
plt.plot(years, education, marker='o', label='Образование')
plt.plot(years, healthcare_social_services, marker='o', label='Здравоохранение и социальные услуги')

plt.xlabel('Год')
plt.ylabel('НЗП, рублей')
plt.legend(loc=2)

fig_html = mpld3.fig_to_html(fig)
components.html(fig_html, height=600)


st.write('''
**Выводы**: 

* НЗП по всем видам деятельности растет с каждым годом исходя из данных Ростата.
* НЗП в строительстве превышает большей частью НЗП в образовании и здравоохранении.
* НЗП в образовании в целом ниже, чем заработные платы в строительстве и здравохранении.
''')


st.header('Инфляция', anchor='inflation')

df_inflation = get_inflation()
st.dataframe(df_inflation)


st.header('Среднемесячная реальная заработная плата по трем видам экономической деятельности за 2000-2023 гг.', anchor='salaries-real')

df_salaries_real = get_salaries_real()
st.dataframe(df_salaries_real)

st.write('По данным видно, что **значения заработных плат** за каждый год **снизились**.')


st.header('Влияние инфляции на изменение заработной платы по сравнению с предыдущим годом', anchor='inflation-influence')

df_inflation_influence = get_inflation_influence()
st.dataframe(df_inflation_influence)

st.write('**Вывод**: из расчетов видно, что по всем трем областям идет резкое снижение **ИРЗП** в 2009-2010 гг., '
         'далее идут периоды как роста, так и снижения ИРЗП, с последующим увеличением ИРЗП в 2023 году.')

st.write('Отобразим график влияния инфляция на изменение реальной заработной платы по сравнению с предыдущим годом:')

fig = plt.figure(figsize=(8, 4))

years = df_inflation_influence['year']

construction_real_index = df_inflation_influence['construction_real_salary_index']
education_real_index = df_inflation_influence['education_real_salary_index']
healthcare_real_index = df_inflation_influence['healthcare_social_services_real_salary_index']

plt.plot(years, construction_real_index, marker='o', label='Строительство')
plt.plot(years, education_real_index, marker='o', label='Образование')
plt.plot(years, healthcare_real_index, marker='o', label='Зравоохранение и социальные услуги')


plt.title('Влияние инфляции на изменение реальной заработной платы по сравнению с предыдущим годом (%)')

plt.xlabel('Год')
plt.ylabel('ИРЗП %')
plt.legend(loc=9)
plt.grid()
st.pyplot(fig)

st.write('Построим графики изменения реальных и номинальных заработных плат по годам для выбранных видов экономической деятельности:')

years = df_salaries_real['year']

construction_real = df_salaries_real['construction']
fig = plt.figure(figsize=(6, 3))
plt.plot(years, construction_real, marker='o', label='РЗП, рублей')
plt.plot(years, construction, marker='o', label='НЗП, рублей')

plt.title('Строительство')
plt.legend(loc=2)
plt.grid()
st.pyplot(fig)


education_real = df_salaries_real['education']
fig = plt.figure(figsize=(6, 3))
plt.plot(years, education_real, marker='o', label='РЗП, рублей')
plt.plot(years, education, marker='o', label='НЗП, рублей')

plt.title('Образование')
plt.legend(loc=2)
plt.grid()
st.pyplot(fig)


healthcare_real = df_salaries_real['healthcare_social_services']
fig = plt.figure(figsize=(6, 3))
plt.plot(years, healthcare_real, marker='o', label='РЗП, рублей')
plt.plot(years, healthcare_social_services, marker='o', label='НЗП, рублей')

plt.title('Здравоохранение и социальные услуги')
plt.legend(loc=2)
plt.grid()
st.pyplot(fig)

st.write('На всех трех графиках видно, что НЗП и РЗП сначала идут почти вровень, но потом можно наблюдать снижение РЗП относительно НЗП.')


with st.sidebar:
    image = Image.open('increase_chart.jpg')
    st.image(image, width=280)

    st.write('Меню')
    st.markdown(':credit_card: [Номинальная заработная плата](#salaries)')
    st.markdown(':bank: [Инфляция](#inflation)')
    st.markdown(':bar_chart: [Реальная заработная плата](#salaries-real)')
    st.markdown(':chart_with_upwards_trend: [Влияние инфляции](#inflation-influence)')
