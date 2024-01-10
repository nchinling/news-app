# News App

## Overview

NewsHub is a web application that provides users with the latest news articles. Users can view a list of news articles, search for specific topics, and read more about interesting articles. The app is developed using Flask and several http libraries. The live news sources are obtained from Mediastack API with a 30 minute delay. 

## Features

1. **Latest News Display:**
   - The homepage displays the latest 10 news articles by default.
   - Articles are categorised, showing details such as title, category, description, source, image, and published date and time.

2. **Null image handling:**
   - Null images are replaced with an alternative image.

2. **Search Functionality:**
   - Users can perform searches by entering keywords in the search bar.
   - The application allows users to search for specific topics of interest.

## Getting Started

### Prerequisites

- Python (3.x recommended)
- Flask
- Requests library
- Bootstrap (CSS framework)
- Mediastack API key

### Installation

1. Clone the repository:

   ```bash
   git clone <repository-url>
   cd <repository-direcotry>


### Usage
1. Visit the homepage to see the latest news.
2. Use the search bar to find news articles related to specific topics.
3. Explore details of each article, including the title, category, author, description, source, image, and published date.

### Acknowledgements
- MediaStack API for providing the latest news data.