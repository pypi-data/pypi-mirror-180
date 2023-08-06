<a name="readme-top"></a>

<!-- [![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url] -->
[![MIT License][license-shield]][license-url]
<!-- [![LinkedIn][linkedin-shield]][linkedin-url] -->



<br />
<div align="center">

  <h3 align="center">Tiny Data Analytics Tool</h3>

  <p align="center">
    A tiny data analytics tool from when I started learning Python
    <br />
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#license">License</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

This is a tiny Data Analytics Tool from when started learning Python in 2019. I don't maintain it and decided primarily to publish it for a friend of mine, who needed such “tiny” tool for his local Data Analytics Scripts. An Example of how to use is provided below under the `Getting Started` section.

That said... This is a tiny tool encompassing a GUI for flexibly organizing Data Analytics related tasks/functions and adding custom User Input Fields if needed. It builds up a Tkinter GUI where custom functions can be started and if needed provide User Input. It can plainly execute some logic or render Matplotlib Graphs.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Built With

[![Python][Python]][Python-url]


<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started
```python

import pandas as pd
from tiny_data_analytics_tool.TinyDataAnalyticsTool import TinyDataAnalyticsTool
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use("TkAgg")

def myFunc(*args, **kwargs):
    # Nested dictionary of User Input including Tkinter Objects for further manipulations if required
    user_inputs : dict = kwargs.get('user_inputs') 
    # Trimmed only if User did NOT select option 'All' 
    trimmed_data_based_on_user_input :pd.DataFrame = kwargs.get('data') 
    print(user_inputs)
    print(trimmed_data_based_on_user_input)
    plt.hist(trimmed_data_based_on_user_input["Column1"])
    plt.show()

def main():                      
    #Import: Use the function name (e.g. myFunc) consistent 

    # Read your Data as Pandas Data Frame
    data = pd.DataFrame({'Column1': [1,2,3,4,5],'Column2':[5,4,3,2,1]})

    #Here you give as parameter your Data
    dict_data = {'myFunc' : data}

    #Here you specify the function which shall be called in the Analytics Class above
    func_dict = {"myFunc" : myFunc}

    #Here you specify special options for your DropDown menu, for example if the analysis should be based on relative or absoloute values
    #You can pass multiple special dicts in form of a nested dict
    dict_special_dropdown_options = {'myFunc' : {'Method (Parameters to choose from as a User not in dataset)' : ['Mean' , 'Median', 'Standarddeviation']}}

    #Here you specify Parameters which correspond to the column names in the dataFrame
    option_parameters_from_dataset_columns = {"myFunc" : ['Column1', 'Column2']}

    #here you can change the name of the column names for aesthetic reasons.
    func_parameters_desc = {"myFunc" : {'Column1' : 'Choice 1', 'Column2' : 'Choice 2'}}
    
    #Create the Gui and insert the parameters
    TinyDataAnalyticsTool(func_dict, option_parameters_from_dataset_columns, dict_data = dict_data,
            func_parameters_display_descr=func_parameters_desc,
            dict_special_dropdown_options=dict_special_dropdown_options)

if __name__ == '__main__':
    main()
```

### Prerequisites

Python >=3.6


### Installation


pip install TinyDataAnalyticsTool

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

[contributors-shield]: https://img.shields.io/github/contributors/othneildrew/Best-README-Template.svg?style=for-the-badge
[contributors-url]: https://github.com/othneildrew/Best-README-Template/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/othneildrew/Best-README-Template.svg?style=for-the-badge
[forks-url]: https://github.com/othneildrew/Best-README-Template/network/members
[stars-shield]: https://img.shields.io/github/stars/othneildrew/Best-README-Template.svg?style=for-the-badge
[stars-url]: https://github.com/othneildrew/Best-README-Template/stargazers
[issues-shield]: https://img.shields.io/github/issues/othneildrew/Best-README-Template.svg?style=for-the-badge
[issues-url]: https://github.com/othneildrew/Best-README-Template/issues
[license-shield]: https://img.shields.io/github/license/othneildrew/Best-README-Template.svg?style=for-the-badge
[license-url]: https://github.com/othneildrew/Best-README-Template/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/othneildrew
[product-screenshot]: https://www.ltep-technologies.com/wp-content/uploads/2022/06/ATHINA_LOGO-3.png
[Python]: https://www.python.org/static/community_logos/python-powered-w-100x40.png
[Python-url]: https://www.python.org/
[React.js]: https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB
[React-url]: https://reactjs.org/
[Vue.js]: https://img.shields.io/badge/Vue.js-35495E?style=for-the-badge&logo=vuedotjs&logoColor=4FC08D
[Vue-url]: https://vuejs.org/
[Angular.io]: https://img.shields.io/badge/Angular-DD0031?style=for-the-badge&logo=angular&logoColor=white
[Angular-url]: https://angular.io/
[Svelte.dev]: https://img.shields.io/badge/Svelte-4A4A55?style=for-the-badge&logo=svelte&logoColor=FF3E00
[Svelte-url]: https://svelte.dev/
[Laravel.com]: https://img.shields.io/badge/Laravel-FF2D20?style=for-the-badge&logo=laravel&logoColor=white
[Laravel-url]: https://laravel.com
[Bootstrap.com]: https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white
[Bootstrap-url]: https://getbootstrap.com
[JQuery.com]: https://img.shields.io/badge/jQuery-0769AD?style=for-the-badge&logo=jquery&logoColor=white
[JQuery-url]: https://jquery.com 