# CS 340 Portfolio – Project Two

## Repository Link
https://github.com/Kashishh02/CS340_Portfolio
## Reflection

### Writing Maintainable, Readable, and Adaptable Programs

To write maintainable and adaptable programs, I focus on separation of responsibilities and clear structure. In Project One, I developed a reusable CRUD Python module that handled all database interactions. Instead of embedding database logic directly inside the dashboard application, I kept it separate. This made the code cleaner, easier to debug, and easier to extend.

When building Project Two, I was able to reuse the same CRUD module to connect the dashboard widgets to the MongoDB database. This approach improved efficiency and reduced duplication. If the database logic ever needs to change, I can modify the CRUD module without rewriting the dashboard code. That separation makes the program more maintainable and scalable.

In the future, this CRUD module could be reused in other database-driven applications such as reporting tools, web APIs, or analytics dashboards. It provides a reusable foundation for any project requiring database operations.

---

### My Approach to Problem-Solving as a Computer Scientist

When approaching this project, I first analyzed the requirements provided by Grazioso Salvare. I focused on understanding how data needed to flow from the MongoDB database to the interactive dashboard components. I broke the problem into layers: database structure, CRUD operations, dashboard filtering logic, and visualization.

Compared to earlier assignments in other courses, this project required more system-level thinking. Instead of solving isolated programming exercises, I had to design an integrated solution that connected backend data management with frontend user interaction.

In the future, when creating databases for client requests, I would carefully plan the data schema, ensure proper indexing for performance, and design reusable data access layers. Planning structure before coding prevents unnecessary redesign and improves long-term efficiency.

---

### What Computer Scientists Do and Why It Matters

Computer scientists design and implement systems that transform data into usable solutions. In this project, the dashboard application allows an organization to filter, analyze, and visualize animal rescue data efficiently.

For a company like Grazioso Salvare, this type of system improves decision-making, reduces manual data searching, and increases operational efficiency. Instead of reviewing raw database records, users can interact with a structured dashboard to quickly access relevant information.

Projects like this demonstrate how software development directly supports business operations and organizational goals. By building structured, reusable, and scalable systems, computer scientists help organizations operate more effectively and make informed decisions.
