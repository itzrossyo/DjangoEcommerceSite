# Flask Blog

![GitHub last commit](https://img.shields.io/github/last-commit/itzrossyo/chatBlog?logo=github&style=flat-square)
![GitHub contributors](https://img.shields.io/github/contributors/itzrossyo/chatBlog?logo=github&style=flat-square)
![GitHub language count](https://img.shields.io/github/languages/count/itzrossyo/chatBlog?logo=github&style=flat-square)
![GitHub top language](https://img.shields.io/github/languages/top/itzrossyo/chatBlog?logo=github&style=flat-square)
![W3C Validation](https://img.shields.io/w3c-validation/html?style=flat-square&targetUrl=https://blog.devross.co.uk/)

## Contents

- [User Experience (UX)](#user-experience-ux)
- [Design](#design)
    - [Colour Scheme](#colour-scheme)
    - [Typography](#typography)
    - [Imagery](#imagery)
    - [Wireframes](#wireframes)
    - [Features](#features)
- [Technologies Used](#technologies-used)
- [Deployment & Local Development](#deployment--local-development)
    - [Deployment](#deployment)
    - [Local Development](#local-development)
    - [How to Fork](#how-to-fork)
    - [How to Clone](#how-to-clone)
- [Testing](#testing)
    - [W3C Validator](#w3c-validator)
    - [Solved Bugs](#solved-bugs)
    - [Known Bugs](#known-bugs)
- [Testing User Stories](#testing-user-stories)
- [Future Developments](#future-developments)
- [Content](#content)

---

## User Experience (UX)

Flask Blog is a website aimed at providing users with engaging and insightful blog content. The site strives to create
an informative and user-friendly experience for visitors interested in exploring various topics through blog posts.

### Key Information

- Name: Flask Blog
- Website: [https://ecom.devross.co.uk](https://blog.devross.co.uk/)
- Purpose: To offer a diverse range of blog content for readers.
- Target Audience: Individuals interested in exploring and reading blog posts on various subjects.

### User Goals

The main goals of users visiting Flask Blog are:

- To discover interesting and well-written blog posts on different topics.
- To easily navigate through the website and find content that matches their interests.
- To engage with the content through comments and feedback.
- To share their favorite blog posts with others.

### First Time Visitor Goals

- Understand the purpose of the website.
- Navigate through different blog categories to discover diverse content.
- Find out how to get involved or leave comments on blog posts.

### Returning Visitor Goals

- Check for new blog posts, updates, or featured content.
- Revisit specific categories for more blog posts on preferred topics.
- Interact with the blog community through comments and discussions.

### Frequent Visitor Goals

- Contribute to the blog community by submitting guest posts or ideas.
- Share blog posts on social media platforms.
- Participate in polls or surveys related to blog content preferences.

## Design

### Wireframes

[Link to wireframes on GitHub](https://github.com/itzrossyo/chatblog-ux/blob/main/Home%20page.png)

### Colour Scheme

The website will use a modern and minimalistic color scheme, primarily consisting of pastel colors, promoting a clean
and inviting visual experience.

### Typography

The font used on the website will be a clean and easily readable sans-serif typeface, ensuring an enjoyable reading
experience for users.

### Imagery

High-quality and relevant images will be strategically used throughout the website to enhance visual appeal and maintain
user engagement.

### Features

- Products that can be placed into your cart
- User Registration and Login for saved address
- paypal checkout

#### Header

The header will be fixed at the top of the page, featuring a navigation menu.

#### Footer

## Technologies Used

- HTML5
- CSS3
- JavaScript
- Python
- django
- bootstrap
- Flask
- SQLAlchemy
- Bcrypt
- Jinja2
- CloudFlare

## Deployment & Local Development

### Deployment

The website is currently deployed at [https://ecom.devross.co.uk/](https://ecom.devross.co.uk/).

### Local Development

To run the website locally, follow these steps:

1. Clone the repository
   from [https://github.com/itzrossyo/blog-flask.git](https://github.com/itzrossyo/DjangoEcommerceSite.git).
2. Open the index.html file in your preferred web browser.

### How to Fork

To fork the Flask Blog repository:

1. Log in (or sign up) to GitHub.
2. Go to the repository for this project, [blog-flask](https://github.com/itzrossyo/DjangoEcommerceSite).
3. Click the Fork button in the top right corner.

### How to Clone

To clone the Flask Blog repository:

1. Log in (or sign up) to GitHub.
2. Go to the repository for this project, [blog-flask](https://github.com/itzrossyo/DjangoEcommerceSite).
3. Click on the code button, select whether you would like to clone with
   HTTPS https://github.com/itzrossyo/DjangoEcommerceSite.git and copy the link shown.
4. Open the terminal in your code editor and change the current working directory to the location you want to use for
   the cloned directory.
5. Type 'git clone' into the terminal and then paste the link you copied in step 3. Press enter.

## Testing

- Laptop
    - MacBook Pro 13 2019
    - HP Omen 15 inch
    - Dell XPS
- Mobile
    - Oppo Find X5 Lite (6.42inch)
    - Samsung S22 Ultra
    - iPhone 13 Pro Max
    - iPhone 12 Max
    - iPhone 12
    - Google Pixel 6
- Browsers
    - Google Chrome
    - Firefox
    - Opera
    - Safari

| Feature                 | Expected Outcome                                                                                                           | Testing Performed                                                                                                              | Result                                              | Pass/Fail |
|-------------------------|----------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------|-----------|
| 404 Error Page          | This should come up when the user page won't load or is down, giving them a custom special message.                        | Accessed a non-existing URL to trigger the 404 page. Verified the custom message.                                              | Custom 404 page appeared with the correct message.  | Pass      |
| Informative Blog Posts  | Users can explore diverse blog posts on different topics.                                                                  | Browsed through various blog categories and read different blog posts.                                                         | Blog posts displayed and covered a range of topics. | Pass      |
| User Registration/Login | A user registration and login system allow users to create accounts, log in, and securely access personalized features.    | Attempted to register new user accounts and log in with existing accounts. Verified account creation and secure login process. | User accounts created, and login process secure.    | Pass      |
| Dropdown Menu           | Once the hamburger button has been pressed on mobile, a dropdown menu will slide in from the left with a smooth animation. | This test was performed by clicking on the hamburger menu to see if the dropdown menu will show up smoothly.                   | This worked as intended.                            | Pass      |

---

### W3C Validator

[Link to GitHub W3C Validation images](https://raw.githubusercontent.com/itzrossyo/chatblog-ux/main/cssvalidation.png?token=GHSAT0AAAAAACIBVAZLMLTRKJ2WLFJVLYAKZKRMJMQ)

### Solved Bugs

| Num | Bug                                                           | How I Solved the Bug                                                                                                                                       |
|-----|---------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1   | images was not loading when i was trying to run on the server | changed to static  item.product.imageURL                                                                                                                   |
| 2   | Unresponsive Design on Mobile Devices                         | Implemented a responsive design using media queries in CSS. Ensured that the layout, images, and content adjusted appropriately to different screen sizes. |

### Known Bugs

| Known Bugs     | Bug Issue                                                                | Plan to Resolve                        |
|----------------|--------------------------------------------------------------------------|----------------------------------------|
| Paypal new box | A new box appears when you click checkout having to close it to continue | try to see why this opens up a new box |

The website's code will be validated and properly formatted to adhere to industry best practices.

## Testing User Stories

| Testing User Stories |                      | User Story                                                                             | Test Case                                                                                                     | Result                                                   |
|----------------------|----------------------|----------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------|----------------------------------------------------------|
| User Story           | Newcomer Exploration | I want to be able to vist the site and see what products are there and place and order | The user was able to see what products was at the shop and to  add the items to there cart with out loging in | The user was able to check out with items in there cart. |

## Future Developments

I would love to expand on this by incorporating additional features such as:

- A search functionality for users to find specific topics easily.
- Integration with social media platforms for seamless sharing of blog posts.

### Content

The blog content will continue to cover a wide range of topics, ensuring diversity and relevance to various reader
interests.

## Prerequisites

#### Homelab

- I'm using promox to run many home project servers.
- As one server is running Windows server 2019.
- my domain Devross.co.uk things are very simple so simply.
- having a fresh installation up and by going to [cloudflare](https://www.cloudflare.com/en-gb/e) you can install there
  services to the machine.
- creating a tunnel without using my main website to show simple projects I am able to just run tunnels that allow me to
  direct all traffic though there services without exposing ips or ports.
- By doing this all you need is a subdomain before your domain what type of service "http, https, unix, ssh , TCP," the
  list goes on once you have picked your service simply put your ip in that your app is running on followed by the port
  save the changes and your site is live.
