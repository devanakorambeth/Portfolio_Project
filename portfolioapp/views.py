from django.shortcuts import render
from django.views.generic import View
from django.http import JsonResponse

# Create your views here.

class AboutView(View):
    def get(self,request):
        data={
            "ID":1,
            "full_name":"anagha",
            "title":"python django React Fullstack Intern",
            "bio":"A passionate developer and researcher building scalable applications",
            "DOB":"29/01/2000",
            "email":"anagha@gmail.com",
            "contact":9876543212,
            "location":"kakanad",
            "Github_URL" : "https://github.com/in/devana08",
            "linkedin_URL" : "https://Linkedin.com/in/devana08"
        }
        return JsonResponse(data)
    
class Educationview(View):
    def get(self,request):
        data={
        "id": 101, 
        "institution": "Luminar", 
        "course": "Python Full Stack", 
        "university": "ABC University", 
        "location": "Cochin", 
        "starting_year": "June 2026", 
        "ending_year": "January 2027", 
        "cgpa": "7.5", 
        "description": "Completed Python Full Stack Development."
        }     
        return JsonResponse(data)
    
class Projectview(View):
    def get(self,request):
        projects=[ 
         {  
        "id": 1, 
        "title": "DietLense", 
        "short_description": "AI-powered food recognition application.", 
        "long_description": "An application that analyzes food images and provides nutritional information.",
        "technologies_used": [ "Python", "Django", "Google GenAI SDK" ], 
        "live_url": "https://dietlense.example.com", 
        "github_url": "https://github.com/username/dietlense", 
        "image_url": "https://example.com/dietlense.jpg", 
        "featured": "true"
         },
         {
        "id": 2, 
        "title": "Interview Prep Blog", 
        "short_description": "Educational application for programming interviews.", 
        "long_description": "A platform for practicing technical interview questions and reading programming articles.", 
        "technologies_used": [ "Python", "Django", "JavaScript" ], 
        "live_url": "https://prep.example.com", 
        "github_url": "https://github.com/username/interview-prep", 
        "image_url": "https://example.com/interview.jpg", 
        "featured": "true"
         },
         ] 
        return JsonResponse(projects ,safe=False)
    
class Skillsview(View):
    def get(self,request):
        skills=[
        { 
        "id": 1, 
        "skill_name": "Python", 
        "category": "Programming Language", 
        "proficiency": "Advanced", 
        "years_of_experience": 4 
        },
        {
        "id": 2, 
        "skill_name": "Django", 
        "category": "Backend", 
        "proficiency": "Advanced", 
        "years_of_experience": 3
        },
        { 
        "id": 3, 
        "skill_name": "React", 
        "category": "Frontend", 
        "proficiency": "Intermediate", 
        "years_of_experience": 2 
} 
]
        return JsonResponse(skills,safe=False)
        
         
