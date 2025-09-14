#!/usr/bin/env python3
"""
Health Administrative Tool - Demo Script
Demonstrates the key features of the AI-powered healthcare system
"""

import requests
import json
import time
from datetime import datetime, timedelta

class HealthAdminDemo:
    def __init__(self, base_url="http://localhost:8000/api"):
        self.base_url = base_url
        self.auth_token = None
        self.demo_user = None
        
    def print_header(self, title):
        """Print a formatted header"""
        print(f"\n{'='*60}")
        print(f"🏥 {title}")
        print(f"{'='*60}")
    
    def print_step(self, step, description):
        """Print a step with description"""
        print(f"\n{step}. {description}")
        print("-" * 40)
    
    def check_server(self):
        """Check if the server is running"""
        try:
            response = requests.get(f"{self.base_url.replace('/api', '')}/health", timeout=5)
            if response.status_code == 200:
                print("✅ Server is running and healthy")
                return True
            else:
                print(f"❌ Server returned status code: {response.status_code}")
                return False
        except requests.exceptions.RequestException as e:
            print(f"❌ Cannot connect to server: {str(e)}")
            print("Please make sure the server is running: python main.py")
            return False
    
    def register_demo_user(self):
        """Register a demo user"""
        self.print_step(1, "Registering Demo User")
        
        user_data = {
            "username": "demo_provider",
            "email": "demo@healthadmin.com",
            "full_name": "Dr. Demo Provider",
            "password": "demo123",
            "role": "provider"
        }
        
        try:
            response = requests.post(f"{self.base_url}/auth/register", json=user_data)
            if response.status_code == 200:
                self.demo_user = response.json()
                print(f"✅ Demo user created: {self.demo_user['full_name']}")
                return True
            else:
                print(f"❌ Failed to create user: {response.text}")
                return False
        except requests.exceptions.RequestException as e:
            print(f"❌ Error creating user: {str(e)}")
            return False
    
    def login_demo_user(self):
        """Login the demo user"""
        self.print_step(2, "Logging in Demo User")
        
        login_data = {
            "username": "demo_provider",
            "password": "demo123"
        }
        
        try:
            response = requests.post(f"{self.base_url}/auth/login", json=login_data)
            if response.status_code == 200:
                data = response.json()
                self.auth_token = data["access_token"]
                print("✅ Successfully logged in")
                return True
            else:
                print(f"❌ Login failed: {response.text}")
                return False
        except requests.exceptions.RequestException as e:
            print(f"❌ Error logging in: {str(e)}")
            return False
    
    def get_auth_headers(self):
        """Get authorization headers"""
        return {"Authorization": f"Bearer {self.auth_token}"}
    
    def create_demo_patients(self):
        """Create demo patients"""
        self.print_step(3, "Creating Demo Patients")
        
        patients_data = [
            {
                "patient_id": "DEMO001",
                "first_name": "John",
                "last_name": "Smith",
                "date_of_birth": "1985-03-15",
                "gender": "Male",
                "blood_type": "O+",
                "phone": "(555) 123-4567",
                "email": "john.smith@email.com",
                "allergies": "Penicillin, Shellfish",
                "medical_conditions": "Hypertension, Type 2 Diabetes",
                "medications": "Metformin 500mg, Lisinopril 10mg",
                "insurance_provider": "Blue Cross Blue Shield",
                "insurance_number": "BC123456789"
            },
            {
                "patient_id": "DEMO002",
                "first_name": "Sarah",
                "last_name": "Johnson",
                "date_of_birth": "1992-07-22",
                "gender": "Female",
                "blood_type": "A-",
                "phone": "(555) 987-6543",
                "email": "sarah.johnson@email.com",
                "allergies": "None known",
                "medical_conditions": "Asthma",
                "medications": "Albuterol inhaler PRN",
                "insurance_provider": "Aetna",
                "insurance_number": "AET987654321"
            },
            {
                "patient_id": "DEMO003",
                "first_name": "Michael",
                "last_name": "Brown",
                "date_of_birth": "1978-11-08",
                "gender": "Male",
                "blood_type": "B+",
                "phone": "(555) 456-7890",
                "email": "michael.brown@email.com",
                "allergies": "Latex",
                "medical_conditions": "High Cholesterol, GERD",
                "medications": "Atorvastatin 20mg, Omeprazole 20mg",
                "insurance_provider": "Cigna",
                "insurance_number": "CIG456789123"
            }
        ]
        
        created_patients = []
        
        for patient_data in patients_data:
            try:
                response = requests.post(
                    f"{self.base_url}/patients/",
                    json=patient_data,
                    headers=self.get_auth_headers()
                )
                if response.status_code == 200:
                    patient = response.json()
                    created_patients.append(patient)
                    print(f"✅ Created patient: {patient['first_name']} {patient['last_name']} (ID: {patient['patient_id']})")
                else:
                    print(f"❌ Failed to create patient {patient_data['patient_id']}: {response.text}")
            except requests.exceptions.RequestException as e:
                print(f"❌ Error creating patient {patient_data['patient_id']}: {str(e)}")
        
        return created_patients
    
    def create_demo_interactions(self, patients):
        """Create demo patient interactions"""
        self.print_step(4, "Creating Demo Patient Interactions")
        
        interactions_data = [
            {
                "patient_id": patients[0]["id"],
                "interaction_type": "appointment",
                "notes": "Annual checkup. Patient reports feeling well. Blood pressure slightly elevated at 140/90. Discussed lifestyle modifications including diet and exercise. Patient is compliant with medications.",
                "outcome": "successful",
                "satisfaction_rating": 4,
                "follow_up_required": True
            },
            {
                "patient_id": patients[1]["id"],
                "interaction_type": "call",
                "notes": "Follow-up call regarding asthma management. Patient reports good control with current medication. No recent exacerbations. Reviewed proper inhaler technique.",
                "outcome": "successful",
                "satisfaction_rating": 5,
                "follow_up_required": False
            },
            {
                "patient_id": patients[2]["id"],
                "interaction_type": "appointment",
                "notes": "Follow-up for cholesterol management. Lab results show improvement in LDL levels. Patient reports some GI upset with current statin. Discussed alternative options.",
                "outcome": "successful",
                "satisfaction_rating": 3,
                "follow_up_required": True
            }
        ]
        
        created_interactions = []
        
        for interaction_data in interactions_data:
            try:
                response = requests.post(
                    f"{self.base_url}/patients/{interaction_data['patient_id']}/interactions",
                    json=interaction_data,
                    headers=self.get_auth_headers()
                )
                if response.status_code == 200:
                    interaction = response.json()
                    created_interactions.append(interaction)
                    print(f"✅ Created interaction: {interaction['interaction_type']} for patient {interaction['patient_id']}")
                else:
                    print(f"❌ Failed to create interaction: {response.text}")
            except requests.exceptions.RequestException as e:
                print(f"❌ Error creating interaction: {str(e)}")
        
        return created_interactions
    
    def demonstrate_ai_analysis(self, patients):
        """Demonstrate AI analysis features"""
        self.print_step(5, "Demonstrating AI Analysis")
        
        if not patients:
            print("❌ No patients available for AI analysis")
            return
        
        patient = patients[0]  # Use first patient
        
        print(f"🤖 Generating AI insights for {patient['first_name']} {patient['last_name']}...")
        
        analysis_data = {
            "patient_id": patient["id"],
            "analysis_type": "relationship",
            "additional_context": "Patient has been with the practice for 2 years. Generally compliant with treatment plans."
        }
        
        try:
            response = requests.post(
                f"{self.base_url}/patients/{patient['id']}/ai-analysis",
                json=analysis_data,
                headers=self.get_auth_headers()
            )
            
            if response.status_code == 200:
                result = response.json()
                print("✅ AI analysis completed successfully!")
                
                if result.get("success"):
                    analysis = result.get("analysis", {})
                    print("\n📊 AI Analysis Results:")
                    for key, value in analysis.items():
                        if value:
                            print(f"  • {key.replace('_', ' ').title()}: {value}")
                else:
                    print("⚠️ AI analysis completed with fallback data")
                    fallback = result.get("fallback_data", {})
                    for key, value in fallback.items():
                        if value:
                            print(f"  • {key.replace('_', ' ').title()}: {value}")
            else:
                print(f"❌ AI analysis failed: {response.text}")
                
        except requests.exceptions.RequestException as e:
            print(f"❌ Error running AI analysis: {str(e)}")
    
    def show_dashboard_stats(self):
        """Show dashboard statistics"""
        self.print_step(6, "Displaying Dashboard Statistics")
        
        try:
            response = requests.get(
                f"{self.base_url}/dashboard/stats",
                headers=self.get_auth_headers()
            )
            
            if response.status_code == 200:
                stats = response.json()
                print("📊 Dashboard Statistics:")
                print(f"  • Total Patients: {stats.get('total_patients', 0)}")
                print(f"  • Active Patients: {stats.get('active_patients', 0)}")
                print(f"  • Today's Interactions: {stats.get('total_interactions_today', 0)}")
                print(f"  • Follow-ups Needed: {stats.get('patients_needing_followup', 0)}")
                print(f"  • Average Relationship Score: {stats.get('average_relationship_score', 0)}/100")
                print(f"  • Recent AI Insights: {stats.get('recent_ai_insights', 0)}")
            else:
                print(f"❌ Failed to get dashboard stats: {response.text}")
                
        except requests.exceptions.RequestException as e:
            print(f"❌ Error getting dashboard stats: {str(e)}")
    
    def show_recent_activity(self):
        """Show recent activity"""
        self.print_step(7, "Displaying Recent Activity")
        
        try:
            response = requests.get(
                f"{self.base_url}/dashboard/recent-activity",
                headers=self.get_auth_headers()
            )
            
            if response.status_code == 200:
                activities = response.json()
                print("📈 Recent Activity:")
                
                if activities:
                    for i, activity in enumerate(activities[:5], 1):
                        timestamp = activity.get('timestamp', 'Unknown time')
                        action = activity.get('action', 'Unknown action')
                        patient_name = activity.get('patient_name', 'Unknown patient')
                        print(f"  {i}. {action} - {patient_name} ({timestamp})")
                else:
                    print("  No recent activity to display")
            else:
                print(f"❌ Failed to get recent activity: {response.text}")
                
        except requests.exceptions.RequestException as e:
            print(f"❌ Error getting recent activity: {str(e)}")
    
    def run_demo(self):
        """Run the complete demo"""
        self.print_header("Health Administrative Tool - AI-Powered Demo")
        
        print("This demo will showcase the key features of the Health Administrative Tool:")
        print("• User registration and authentication")
        print("• Patient management with encrypted data")
        print("• Patient interaction tracking")
        print("• AI-powered insights and analysis")
        print("• Dashboard statistics and monitoring")
        
        # Check server
        if not self.check_server():
            return False
        
        # Register and login user
        if not self.register_demo_user():
            print("⚠️ User might already exist, trying to login...")
        
        if not self.login_demo_user():
            return False
        
        # Create demo data
        patients = self.create_demo_patients()
        if not patients:
            print("❌ No patients created, cannot continue demo")
            return False
        
        # Create interactions
        interactions = self.create_demo_interactions(patients)
        
        # Demonstrate AI features
        self.demonstrate_ai_analysis(patients)
        
        # Show dashboard
        self.show_dashboard_stats()
        self.show_recent_activity()
        
        # Final summary
        self.print_header("Demo Complete!")
        print("🎉 The Health Administrative Tool demo has been completed successfully!")
        print("\nKey features demonstrated:")
        print("✅ Secure user authentication and authorization")
        print("✅ Patient data management with encryption")
        print("✅ Patient interaction tracking and logging")
        print("✅ AI-powered analysis and insights")
        print("✅ Real-time dashboard and statistics")
        print("✅ HIPAA-compliant audit logging")
        
        print(f"\n📱 Access the application:")
        print(f"• Web Interface: http://localhost:8000")
        print(f"• API Documentation: http://localhost:8000/api/docs")
        print(f"• Desktop GUI: python start_gui.py")
        
        print(f"\n🔑 Demo Credentials:")
        print(f"• Username: demo_provider")
        print(f"• Password: demo123")
        
        return True

def main():
    """Main function"""
    demo = HealthAdminDemo()
    
    try:
        success = demo.run_demo()
        if success:
            print("\n🎯 Demo completed successfully!")
        else:
            print("\n❌ Demo failed. Please check the server and try again.")
    except KeyboardInterrupt:
        print("\n\n⏹️ Demo interrupted by user.")
    except Exception as e:
        print(f"\n❌ Demo failed with error: {str(e)}")

if __name__ == "__main__":
    main()
