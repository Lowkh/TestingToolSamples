# Locust Load Test for www.np.edu.sg
# This script simulates realistic user behavior on the Ngee Ann Polytechnic website
# 
# Installation:
#   pip install locust pyquery
#
# Running the test:
#   locust -f np_locustfile.py --host=https://www.np.edu.sg
#   Then open http://localhost:8089 in your browser

from locust import HttpUser, task, between, TaskSet
import random


class StudentBehavior(TaskSet):
    """Simulates a prospective student browsing the website"""
    
    def on_start(self):
        """Initialize when a simulated student starts"""
        self.client.get("/", name="Homepage")
    
    @task(3)
    def view_homepage(self):
        """Explore the homepage"""
        self.client.get("/", name="Homepage")
    
    @task(4)
    def browse_courses(self):
        """Browse course offerings"""
        # Adjust these paths based on actual NP website structure
        endpoints = [
            "/courses",
            "/courses/engineering",
            "/courses/it",
            "/courses/business",
        ]
        self.client.get(random.choice(endpoints), name="Browse Courses")
    
    @task(2)
    def explore_student_life(self):
        """Explore student life section"""
        self.client.get("/student-life", name="Student Life")
    
    @task(2)
    def view_admissions(self):
        """Check admissions information"""
        self.client.get("/admissions", name="Admissions")
    
    @task(1)
    def download_prospectus(self):
        """Download prospectus or documents"""
        self.client.get("/resources", name="Resources")


class ParentBehavior(TaskSet):
    """Simulates a parent researching the polytechnic"""
    
    def on_start(self):
        """Initialize when a parent starts"""
        self.client.get("/", name="Homepage")
    
    @task(2)
    def view_homepage(self):
        """Visit homepage"""
        self.client.get("/", name="Homepage")
    
    @task(3)
    def explore_facilities(self):
        """Explore campus and facilities"""
        self.client.get("/campus", name="Campus Info")
    
    @task(2)
    def check_achievements(self):
        """Check achievements and rankings"""
        self.client.get("/about", name="About NP")
    
    @task(2)
    def contact_info(self):
        """Look for contact information"""
        self.client.get("/contact", name="Contact")


class SearchUser(TaskSet):
    """Simulates a user using search functionality"""
    
    def on_start(self):
        """Initialize when a search user starts"""
        self.client.get("/", name="Homepage")
    
    @task(5)
    def search_courses(self):
        """Perform course search"""
        search_terms = [
            "engineering",
            "business",
            "information technology",
            "design",
            "diploma",
        ]
        query = random.choice(search_terms)
        self.client.get(f"/search?q={query}", name="Search")
    
    @task(2)
    def view_search_results(self):
        """Browse search results"""
        self.client.get("/search-results", name="Search Results")


class StudentUser(HttpUser):
    """Prospective student visiting NP website"""
    wait_time = between(2, 8)
    tasks = [StudentBehavior]


class ParentUser(HttpUser):
    """Parent researching NP for their child"""
    wait_time = between(5, 15)
    tasks = [ParentBehavior]


class SearcherUser(HttpUser):
    """User looking for specific information via search"""
    wait_time = between(1, 4)
    tasks = [SearchUser]
