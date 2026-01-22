# Sehat-Fahm: Multi-agent medical analysis system with Urdu voice accessibility for rural healthcare.

## The Problem
**Bridging the Gap in Rural Healthcare Accessibility**

In Pakistan, particularly in rural areas, patients face a "last-mile" challenge in healthcare diagnostics. While patients may travel to cities to conduct necessary lab tests, interpreting the resulting reports creates a critical bottleneck:
1.  **Language Barrier**: Medical reports are almost exclusively generated in English, using complex medical terminology. This makes them unintelligible to the vast majority of the rural population who speak Urdu or regional dialects.
2.  **Doctor Scarcity**: Rural areas suffer from a severe shortage of qualified doctors. Patients often have to travel long distances or wait days just to have a doctor read a report and confirm if their condition is serious.
3.  **Anxiety & Delay**: The inability to read their own reports leads to unnecessary anxiety or, worse, delays in seeking critical care because the urgency of the results isn't understood immediately.

**Sehat-Fahm** addresses this specific crisis by acting as an intelligent intermediary—instantly translating complex English medical data into spoken Urdu, empowering patients to understand their health status immediately without waiting for a consultation.

## Overview

**Sehat-Fahm** (سہت فہم) is an intelligent multi-agent system designed to automate medical lab report analysis and provide accessible health insights. The system leverages advanced AI technologies including LangGraph multi-agent orchestration, RAG (Retrieval-Augmented Generation) pipelines, and natural language processing to make medical information understandable for non-medical users, with special emphasis on Urdu language accessibility.

## Key Features

### 🤖 Multi-Agent Architecture
- **LangGraph-based Agent System**: Engineered a sophisticated multi-agent workflow using LangGraph to orchestrate specialized AI agents
- **Two Specialized Agents**:
  - **Extractor Agent**: Extracts comprehensive textual content from medical PDF reports without summarization or interpretation
  - **Doctor Agent**: Analyzes extracted reports and provides detailed, easy-to-understand medical insights

### 🧠 RAG Pipeline with Research-Backed Knowledge
- **ChromaDB Vector Store**: Persistent vector database storing medical knowledge from MedlinePlus
- **HuggingFace Embeddings**: Uses `all-MiniLM-L6-v2` model for semantic search and document retrieval
- **MedlinePlus Integration**: Automated web crawler that ingests medical lab test information from MedlinePlus.gov
- **PubMed Integration**: Access to up-to-date medical research through PubMed query tool

### 🌐 Urdu Language Accessibility
- **Google Translator Integration**: Automatic translation of medical insights from English to Urdu
- **Text-to-Speech (gTTS)**: Converts Urdu text to natural speech for audio playback
- **Bilingual Interface**: Streamlit UI supports both English and Urdu display

### 🎨 Real-Time Streamlit Interface
- **Interactive Web Application**: Modern, user-friendly interface for uploading and analyzing medical reports
- **Real-Time Processing**: Live analysis with progress indicators
- **Audio Playback**: Integrated audio player for Urdu voice output

## Architecture

### System Components
