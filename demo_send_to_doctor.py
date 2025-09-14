#!/usr/bin/env python3
"""
Demo script showing the Send AI Conversations to Doctor feature
"""

import customtkinter as ctk
import tkinter as tk
from tkinter import messagebox
import requests
import json
from datetime import datetime

class SendToDoctorDemo:
    def __init__(self):
        self.root = ctk.CTk()
        self.root.title("Send AI Conversations to Doctor - Demo")
        self.root.geometry("800x600")
        
        # Mock conversation data
        self.mock_conversation = [
            {"sender": "User", "message": "Hello, I have some questions about my health", "timestamp": "10:30", "type": "user"},
            {"sender": "AI Assistant", "message": "Hello! I'm here to help with your health questions. What would you like to know?", "timestamp": "10:30", "type": "ai"},
            {"sender": "User", "message": "I've been experiencing headaches lately and I'm worried", "timestamp": "10:31", "type": "user"},
            {"sender": "AI Assistant", "message": "I understand your concern about headaches. While I can provide general information, it's important to consult with a healthcare provider for proper evaluation. What other symptoms are you experiencing?", "timestamp": "10:31", "type": "ai"},
            {"sender": "User", "message": "I also have some dizziness and fatigue. Should I be concerned?", "timestamp": "10:32", "type": "user"},
            {"sender": "AI Assistant", "message": "Headaches with dizziness and fatigue can have various causes. I recommend scheduling an appointment with your doctor for a thorough evaluation. In the meantime, ensure you're staying hydrated and getting adequate rest.", "timestamp": "10:32", "type": "ai"},
        ]
        
        self.setup_ui()
    
    def setup_ui(self):
        """Setup the demo interface"""
        # Title
        title_label = ctk.CTkLabel(
            self.root,
            text="📤 Send AI Conversations to Doctor - Demo",
            font=ctk.CTkFont(size=24, weight="bold"),
            text_color="#17A2B8"
        )
        title_label.pack(pady=20)
        
        # Description
        desc_label = ctk.CTkLabel(
            self.root,
            text="This demo shows how healthcare providers can export AI conversations and send them to doctors for review.",
            font=ctk.CTkFont(size=14),
            text_color="#666666"
        )
        desc_label.pack(pady=(0, 20))
        
        # Main content frame
        content_frame = ctk.CTkFrame(self.root)
        content_frame.pack(fill="both", expand=True, padx=20, pady=10)
        
        # Left panel - Conversation preview
        left_frame = ctk.CTkFrame(content_frame)
        left_frame.pack(side="left", fill="both", expand=True, padx=(20, 10), pady=20)
        
        left_title = ctk.CTkLabel(
            left_frame,
            text="💬 Sample AI Conversation",
            font=ctk.CTkFont(size=16, weight="bold"),
            text_color="#2E86AB"
        )
        left_title.pack(pady=(20, 10))
        
        # Conversation display
        self.conversation_display = ctk.CTkTextbox(
            left_frame,
            height=300,
            font=ctk.CTkFont(size=12),
            wrap="word"
        )
        self.conversation_display.pack(fill="both", expand=True, padx=20, pady=(0, 20))
        
        # Load mock conversation
        self.load_mock_conversation()
        
        # Right panel - Export options
        right_frame = ctk.CTkFrame(content_frame)
        right_frame.pack(side="right", fill="both", expand=True, padx=(10, 20), pady=20)
        
        right_title = ctk.CTkLabel(
            right_frame,
            text="📤 Export Options",
            font=ctk.CTkFont(size=16, weight="bold"),
            text_color="#17A2B8"
        )
        right_title.pack(pady=(20, 15))
        
        # Doctor information
        doctor_frame = ctk.CTkFrame(right_frame, fg_color="transparent")
        doctor_frame.pack(fill="x", padx=20, pady=10)
        
        ctk.CTkLabel(doctor_frame, text="Doctor Information:", font=ctk.CTkFont(size=14, weight="bold")).pack(anchor="w")
        
        # Doctor name
        ctk.CTkLabel(doctor_frame, text="Doctor Name:", font=ctk.CTkFont(size=12)).pack(anchor="w", pady=(10, 5))
        self.doctor_name_entry = ctk.CTkEntry(
            doctor_frame,
            height=35,
            font=ctk.CTkFont(size=14),
            placeholder_text="Dr. Smith"
        )
        self.doctor_name_entry.pack(fill="x", pady=(0, 10))
        
        # Doctor email
        ctk.CTkLabel(doctor_frame, text="Doctor Email:", font=ctk.CTkFont(size=12)).pack(anchor="w")
        self.doctor_email_entry = ctk.CTkEntry(
            doctor_frame,
            height=35,
            font=ctk.CTkFont(size=14),
            placeholder_text="doctor@hospital.com"
        )
        self.doctor_email_entry.pack(fill="x", pady=(5, 10))
        
        # Export format
        ctk.CTkLabel(doctor_frame, text="Export Format:", font=ctk.CTkFont(size=12)).pack(anchor="w")
        self.format_var = tk.StringVar(value="pdf")
        format_combo = ctk.CTkComboBox(
            doctor_frame,
            variable=self.format_var,
            values=["pdf", "text", "json"],
            height=35,
            font=ctk.CTkFont(size=14)
        )
        format_combo.pack(fill="x", pady=(5, 15))
        
        # Features list
        features_frame = ctk.CTkFrame(right_frame)
        features_frame.pack(fill="x", padx=20, pady=10)
        
        features_title = ctk.CTkLabel(
            features_frame,
            text="✨ Export Features",
            font=ctk.CTkFont(size=14, weight="bold"),
            text_color="#28A745"
        )
        features_title.pack(pady=(15, 10))
        
        features = [
            "🤖 AI-generated conversation summary",
            "📊 Key topics and insights extraction",
            "⚡ Urgency level assessment",
            "💡 Recommended actions for doctor",
            "👤 Patient context inclusion",
            "📄 Multiple export formats (PDF, Text, JSON)",
            "🔒 Secure data handling",
            "📧 Direct delivery to doctor"
        ]
        
        for feature in features:
            feature_label = ctk.CTkLabel(
                features_frame,
                text=feature,
                font=ctk.CTkFont(size=11),
                text_color="#666666"
            )
            feature_label.pack(anchor="w", padx=15, pady=2)
        
        # Demo button
        demo_btn = ctk.CTkButton(
            right_frame,
            text="🎬 Run Demo Export",
            command=self.run_demo_export,
            height=45,
            font=ctk.CTkFont(size=16, weight="bold"),
            fg_color="#17A2B8",
            hover_color="#138496"
        )
        demo_btn.pack(pady=20)
        
        # Status label
        self.status_label = ctk.CTkLabel(
            right_frame,
            text="Ready to demonstrate the export feature",
            font=ctk.CTkFont(size=12),
            text_color="#28A745"
        )
        self.status_label.pack(pady=(0, 20))
    
    def load_mock_conversation(self):
        """Load mock conversation into the display"""
        self.conversation_display.configure(state="normal")
        self.conversation_display.delete("1.0", "end")
        
        for msg in self.mock_conversation:
            # Format message
            if msg["type"] == "user":
                prefix = "👤"
                color_indicator = "[USER]"
            else:
                prefix = "🤖"
                color_indicator = "[AI]"
            
            self.conversation_display.insert("end", f"[{msg['timestamp']}] {color_indicator} {msg['sender']}:\n")
            self.conversation_display.insert("end", f"{msg['message']}\n\n")
        
        self.conversation_display.configure(state="disabled")
    
    def run_demo_export(self):
        """Run the demo export process"""
        # Validate inputs
        doctor_name = self.doctor_name_entry.get().strip()
        doctor_email = self.doctor_email_entry.get().strip()
        
        if not doctor_name:
            messagebox.showerror("Validation Error", "Please enter the doctor's name.")
            return
        
        if not doctor_email:
            messagebox.showerror("Validation Error", "Please enter the doctor's email address.")
            return
        
        # Update status
        self.status_label.configure(
            text="🔄 Generating export...",
            text_color="#FFC107"
        )
        self.root.update()
        
        # Simulate export process
        self.simulate_export_process(doctor_name, doctor_email)
    
    def simulate_export_process(self, doctor_name, doctor_email):
        """Simulate the export process"""
        import time
        
        # Step 1: Generate AI summary
        self.status_label.configure(text="🤖 Generating AI summary...")
        self.root.update()
        time.sleep(1)
        
        # Step 2: Extract key topics
        self.status_label.configure(text="📊 Extracting key topics...")
        self.root.update()
        time.sleep(1)
        
        # Step 3: Assess urgency
        self.status_label.configure(text="⚡ Assessing urgency level...")
        self.root.update()
        time.sleep(1)
        
        # Step 4: Generate recommendations
        self.status_label.configure(text="💡 Generating recommendations...")
        self.root.update()
        time.sleep(1)
        
        # Step 5: Create export file
        self.status_label.configure(text="📄 Creating export file...")
        self.root.update()
        time.sleep(1)
        
        # Show results
        self.show_export_results(doctor_name, doctor_email)
    
    def show_export_results(self, doctor_name, doctor_email):
        """Show the export results"""
        # Create results dialog
        results_dialog = ctk.CTkToplevel(self.root)
        results_dialog.title("Export Results")
        results_dialog.geometry("600x500")
        results_dialog.transient(self.root)
        results_dialog.grab_set()
        
        # Center dialog
        results_dialog.update_idletasks()
        x = (results_dialog.winfo_screenwidth() // 2) - (600 // 2)
        y = (results_dialog.winfo_screenheight() // 2) - (500 // 2)
        results_dialog.geometry(f"600x500+{x}+{y}")
        
        # Title
        title_label = ctk.CTkLabel(
            results_dialog,
            text="✅ Export Completed Successfully!",
            font=ctk.CTkFont(size=20, weight="bold"),
            text_color="#28A745"
        )
        title_label.pack(pady=20)
        
        # Export details
        details_frame = ctk.CTkFrame(results_dialog)
        details_frame.pack(fill="both", expand=True, padx=20, pady=10)
        
        # Doctor info
        doctor_info = ctk.CTkLabel(
            details_frame,
            text=f"👤 Doctor: {doctor_name}\n📧 Email: {doctor_email}\n📄 Format: {self.format_var.get().upper()}",
            font=ctk.CTkFont(size=14, weight="bold"),
            text_color="#2E86AB"
        )
        doctor_info.pack(pady=(20, 15))
        
        # AI Analysis Results
        analysis_title = ctk.CTkLabel(
            details_frame,
            text="🤖 AI Analysis Results",
            font=ctk.CTkFont(size=16, weight="bold"),
            text_color="#17A2B8"
        )
        analysis_title.pack(pady=(20, 10))
        
        # Mock analysis results
        analysis_results = {
            "summary": "Patient expressed concerns about headaches, dizziness, and fatigue. AI provided general guidance while emphasizing the need for professional medical evaluation.",
            "topics": ["Headaches", "Dizziness", "Fatigue", "Health concerns", "Medical consultation"],
            "urgency": "normal",
            "recommendations": [
                "Schedule appointment with primary care physician",
                "Monitor symptoms and keep a symptom diary",
                "Ensure adequate hydration and rest",
                "Consider neurological evaluation if symptoms persist"
            ]
        }
        
        # Summary
        summary_label = ctk.CTkLabel(
            details_frame,
            text=f"📝 Summary:\n{analysis_results['summary']}",
            font=ctk.CTkFont(size=12),
            text_color="#666666",
            justify="left"
        )
        summary_label.pack(anchor="w", padx=20, pady=5)
        
        # Topics
        topics_text = "🔍 Key Topics: " + ", ".join(analysis_results['topics'])
        topics_label = ctk.CTkLabel(
            details_frame,
            text=topics_text,
            font=ctk.CTkFont(size=12),
            text_color="#666666"
        )
        topics_label.pack(anchor="w", padx=20, pady=5)
        
        # Urgency
        urgency_color = "#28A745" if analysis_results['urgency'] == 'normal' else "#FFC107"
        urgency_label = ctk.CTkLabel(
            details_frame,
            text=f"⚡ Urgency Level: {analysis_results['urgency'].upper()}",
            font=ctk.CTkFont(size=12, weight="bold"),
            text_color=urgency_color
        )
        urgency_label.pack(anchor="w", padx=20, pady=5)
        
        # Recommendations
        recommendations_text = "💡 Recommendations:\n" + "\n".join([f"• {rec}" for rec in analysis_results['recommendations']])
        recommendations_label = ctk.CTkLabel(
            details_frame,
            text=recommendations_text,
            font=ctk.CTkFont(size=12),
            text_color="#666666",
            justify="left"
        )
        recommendations_label.pack(anchor="w", padx=20, pady=5)
        
        # Close button
        close_btn = ctk.CTkButton(
            results_dialog,
            text="✅ Close",
            command=results_dialog.destroy,
            height=40,
            font=ctk.CTkFont(size=14, weight="bold"),
            fg_color="#28A745",
            hover_color="#218838"
        )
        close_btn.pack(pady=20)
        
        # Update main status
        self.status_label.configure(
            text="✅ Export completed successfully!",
            text_color="#28A745"
        )
    
    def run(self):
        """Run the demo"""
        self.root.mainloop()

if __name__ == "__main__":
    print("🚀 Starting Send to Doctor Feature Demo")
    demo = SendToDoctorDemo()
    demo.run()
