# data.py

lessons = {
    "os": {
        "unit 1": "📘 OS Unit 1: Introduction to Operating Systems\n\n- What is an OS?\n- Types: Batch, Time-Sharing, Distributed\n- Functions: Process Management, Memory Management, File Systems"
    },
    "cn": {
        "unit 1": "📘 CN Unit 1: Basics of Computer Networks\n\n- Definition of Network\n- Types: LAN, WAN, MAN\n- OSI & TCP/IP Models\n- Applications of Networking"
    },
    "dbms": {
        "unit 1": "📘 DBMS Unit 1: Introduction\n\n- What is DBMS?\n- Advantages over file system\n- Data Models: Hierarchical, Network, Relational\n- Architecture of DBMS"
    }
}

summaries = {
    "os": "📘 OS Summary: OS manages hardware & software resources. Key concepts include Process Management, Scheduling, Memory Management, and Deadlocks.",
    "cn": "📘 CN Summary: Networks connect computers. Important topics: Protocols, OSI model, IP addressing, Routing, and TCP/IP stack.",
    "dbms": "📘 DBMS Summary: DBMS stores and retrieves user data using SQL. Concepts include ER models, Normalization, Transactions, and Indexing."
}

quizzes = {
    "os": [
        {
            "question": "Which of the following is not a function of an OS?",
            "options": ["Process Management", "Compiler Design", "Memory Management", "File System Management"],
            "answer": "Compiler Design"
        },
        {
            "question": "Which scheduling algorithm is preemptive?",
            "options": ["FCFS", "SJF", "Round Robin", "None of these"],
            "answer": "Round Robin"
        }
    ],
    "cn": [
        {
            "question": "Which layer is responsible for routing?",
            "options": ["Physical", "Network", "Session", "Transport"],
            "answer": "Network"
        },
        {
            "question": "Which of the following is not a type of computer network?",
            "options": ["LAN", "WAN", "PAN", "VAN"],
            "answer": "VAN"
        }
    ],
    "dbms": [
        {
            "question": "What is the full form of DBMS?",
            "options": ["Database Management System", "Data Management Service", "Database Monitoring System", "None of these"],
            "answer": "Database Management System"
        },
        {
            "question": "Which key is used to uniquely identify a row?",
            "options": ["Primary Key", "Foreign Key", "Super Key", "Candidate Key"],
            "answer": "Primary Key"
        }
    ]
}
