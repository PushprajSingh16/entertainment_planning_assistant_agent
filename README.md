# Entertainment Planning Assistant Agent


## Problem Statement & Objectives

### 1. Problem Statement

In today's fast-paced world, planning entertainment activities like movie outings or events requires comprehensive information gathering from multiple sources including theatre locations, show timings, ticket prices, nearby attractions, transportation options, dining choices, and safety considerations. Users often struggle to find all relevant information in one place, leading to inefficient planning and suboptimal entertainment experiences. The challenge is to create an intelligent assistant that can autonomously gather, process, and present detailed entertainment planning information through natural language interaction.

### 2. Project Objectives

- **Develop an AI-powered Entertainment Planning Assistant** that provides comprehensive planning information for movies and events
- **Implement multi-step reasoning capabilities** to decompose user requests into actionable planning components
- **Create a user-friendly web interface** for seamless interaction with the planning system
- **Ensure robust error handling and resource validation** for reliable operation
- **Provide detailed, structured output** covering all aspects of entertainment planning

### 3. Scope of the Project

**In Scope:**
- Movie and event planning for major Indian cities
- Integration with Groq LLM for intelligent content generation
- Web-based user interface with modern design
- RESTful API backend for scalability
- Comprehensive planning information including theatres, timings, prices, attractions, transportation, dining, and safety

**Out of Scope:**
- Real-time ticket booking integration
- Payment processing
- User account management
- Mobile application development
- Real-time data feeds from external APIs

## Proposed Solution

### 1. Key Features

- **Intelligent Planning Agent**: AI-powered agent that generates comprehensive entertainment plans
- **Multi-City Support**: Coverage for 20+ major Indian cities with custom city option
- **Comprehensive Information**: Detailed plans including theatres, timings, pricing, attractions, transportation, dining, weather, and safety
- **Modern Web Interface**: Black and white themed Streamlit frontend with responsive design
- **RESTful API**: FastAPI backend with health monitoring and error handling
- **Configurable Settings**: Environment-based configuration for API keys and model parameters
- **Error Resilience**: Graceful handling of API failures and network issues

### 2. Overall Architecture / Workflow

**Architecture:**
```
┌─────────────────┐    HTTP Requests    ┌─────────────────┐
│   Streamlit     │◄──────────────────►│     FastAPI      │
│   Frontend      │                     │     Backend      │
│   (Port 8501)   │                     │   (Port 8000)    │
└─────────────────┘                     └─────────────────┘
         │                                       │
         │                                       │
         ▼                                       ▼
┌─────────────────┐                     ┌─────────────────┐
│   User Input    │                     │  Planner Agent  │
│   Processing    │                     │                 │
└─────────────────┘                     └─────────────────┘
                                                 │
                                                 ▼
                                       ┌─────────────────┐
                                       │     Groq LLM     │
                                       │   API Service    │
                                       └─────────────────┘
```

**Workflow:**
1. User inputs movie/event and city through web interface
2. Frontend sends request to FastAPI backend
3. Backend PlannerAgent processes request and constructs detailed prompt
4. Agent calls Groq LLM with structured prompt for comprehensive planning
5. LLM generates detailed response covering all planning aspects
6. Backend returns structured JSON response
7. Frontend displays formatted plan with visual elements

### 3. Tools & Technologies Used

**Backend:**
- **FastAPI**: High-performance web framework for building APIs
- **Uvicorn**: ASGI server for running FastAPI applications
- **Groq**: AI platform providing access to Llama language models

**Frontend:**
- **Streamlit**: Python framework for building interactive web applications
- **Custom CSS**: Black and white themed styling for enhanced user experience

**Development & Deployment:**
- **Python 3.13+**: Programming language
- **Virtual Environment**: Isolated Python environment management
- **Environment Variables**: Configuration management with python-dotenv

## Results & Output

### 1. Screenshots / Outputs

**Sample API Response:**
```json
{
  "movie": "Border 2",
  "city": "Indore",
  "plan": "**Border 2 Entertainment Plan**\n\n**Location:** Indore, India\n**Movie:** Border 2\n**Theatres:** PVR Cinemas, Cinepolis, INOX Leisure\n**Show Timings:** Morning: 10 AM-12 PM, Afternoon: 2 PM-5 PM, Evening: 7 PM-10 PM\n**Ticket Prices:** ₹150-₹400\n**Nearby Attractions:** Rajwada Palace, Lal Bagh Palace\n**Transportation:** Auto-rickshaw, taxi, metro\n**Recommended Restaurants:** The Great Kabab Factory, Keventers\n**Weather Considerations:** Pleasant winter temperatures (10-25°C)\n**Safety Tips:** Travel in groups, use reputable transport"
}
```

**Key Interface Elements:**
- Black and white themed web interface with sidebar navigation
- City selection dropdown with 20+ predefined options
- Custom city input for flexibility
- Real-time plan generation with loading indicators
- Structured display of planning information
- Backend health monitoring

### 2. Reports/Dashboards/Models

**API Endpoints:**
- `GET /`: Service status and version information
- `GET /health`: Health check endpoint for monitoring
- `GET /plan?movie={movie}&city={city}`: Main planning endpoint

**Configuration Model:**
- Environment-based settings (.env file)
- Configurable LLM model and temperature
- API key management for Groq integration

### 3. Key Outcomes

- **Successful AI Integration**: Seamless integration with Groq LLM for intelligent content generation
- **Comprehensive Planning**: Single platform providing all entertainment planning information
- **User-Friendly Interface**: Modern black and white themed web application with intuitive navigation
- **Scalable Architecture**: RESTful API design supporting future expansions
- **Error Handling**: Robust error management ensuring reliable user experience
- **Performance**: Fast response times with optimized LLM prompts and token limits

## Conclusion

The Entertainment Planning Assistant Agent represents a successful implementation of AI-powered entertainment planning through a modern web application. The project successfully addresses the challenge of fragmented entertainment information by providing a comprehensive, intelligent planning solution. Key achievements include the development of a multi-step reasoning agent (implemented through structured LLM prompts), creation of a user-friendly web interface, and establishment of a robust backend API. The use of FastAPI and Streamlit frameworks, combined with Groq's advanced language models, resulted in a performant and scalable solution. The project demonstrates the practical application of AI in solving real-world problems, with particular emphasis on user experience and technical reliability.

## Future Scope & Enhancements

**Short-term Enhancements:**
- **Real-time Data Integration**: Connect with external APIs for live theatre availability and pricing
- **User Preferences**: Add user profile system to remember preferences and past plans
- **Offline Mode**: Implement caching for offline access to basic planning information

**Medium-term Features:**
- **Multi-language Support**: Expand to support regional languages and international cities
- **Social Features**: Allow users to share plans and get recommendations from friends
- **Advanced AI Features**: Implement conversation memory for follow-up questions

**Long-term Vision:**
- **Mobile Application**: Develop native mobile apps for iOS and Android
- **Booking Integration**: Direct integration with ticket booking and reservation systems
- **AR Features**: Augmented reality for theatre navigation and seat selection
- **Community Platform**: Build a community-driven entertainment discovery platform

**Technical Improvements:**
- **Microservices Architecture**: Break down into smaller, independently deployable services
- **Database Integration**: Add persistent storage for user data and plan history
- **Analytics Dashboard**: Implement usage analytics and performance monitoring
- **CI/CD Pipeline**: Automated testing and deployment workflows

---

**Built with ❤️ using FastAPI, Streamlit, and Groq AI**


<parameter name="filePath">c:\Users\ANUSHKA\Desktop\entertainment_planning_assistant\README.md
