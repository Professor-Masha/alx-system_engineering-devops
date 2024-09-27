# Postmortem: The Great Database Meltdown of 2024

## Issue Summary

**Duration of the Outage:**  
- **Start:** June 15, 2024, 10:30 AM EAT  
- **End:** July 25, 2024, 12:00 PM EAT  

**Impact:**  
- **Service Affected:** User authentication and data retrieval services.  
- **User Experience:** Users experienced significant delays in login times, with a 75% slowdown in data retrieval requests. Many users were unable to log in for up to 90 minutes.  
- **Affected Users:** Approximately 65% of our active user base (around 15,000 users) experienced issues.

**Root Cause:**  
A sudden surge in database connections exceeded the maximum limit, resulting in a cascading failure that rendered authentication and data retrieval services unresponsive.

---

## Timeline

- **10:30 AM** - **Issue Detected:** Monitoring systems alerted the engineering team to unusually high response times in user authentication.
  
- **10:35 AM** - **Detection Method:** An engineer on duty received a notification from our monitoring tool, Datadog, indicating a spike in connection errors.
  
- **10:40 AM** - **Initial Investigation:** The team investigated the application logs and assumed the root cause was an application bug leading to connection leaks. 

- **10:55 AM** - **Misleading Path:** Engineers focused on optimizing the connection pool settings in our Node.js backend, thinking the issue stemmed from improper connection management.
  
- **11:15 AM** - **Escalation:** The incident was escalated to the Database Administration team for deeper insights, suspecting that the database may have reached its connection limit.
  
- **11:45 AM** - **Resolution:** The Database team identified that the maximum number of connections was exceeded. They promptly increased the connection limit from 150 to 300, and the service began to recover.

---

## Root Cause and Resolution

### Root Cause
The database connections soared beyond the established limit due to a recent increase in user activity following a promotional campaign. The application backend had not been adjusted to handle the increased load, and connection leaks due to unhandled promises in our Node.js code exacerbated the problem. 

### Resolution
To resolve the issue, the Database team increased the maximum connections allowed in the MySQL configuration file:

```sql
SET GLOBAL max_connections = 300;
```

Additionally, the backend code was modified to properly handle promises, ensuring that connections were released back to the pool after each request. Here’s a snippet of the revised code:

```javascript
async function getUserData(userId) {
  const connection = await db.getConnection();
  try {
    const [rows] = await connection.query('SELECT * FROM users WHERE id = ?', [userId]);
    return rows;
  } finally {
    connection.release(); // Ensure the connection is released
  }
}
```

---

## Corrective and Preventative Measures

### Improvements
- Increase awareness of peak traffic times and adapt the infrastructure accordingly.
- Implement better connection pooling strategies and optimize the existing ones.

TODO List
- **Patch Node.js application:** Review and fix all unhandled promise rejections that may lead to connection leaks.
- **Update Database Configurations:** Increase `max_connections` based on expected user load and monitor its performance.
- **Enhance Monitoring:** Add alerts for database connection utilization, ensuring early detection of connection limit issues.
- **Conduct Load Testing:** Simulate traffic spikes in staging to assess performance and identify bottlenecks before they affect users.
- **Documentation:** Update documentation to include postmortem findings and troubleshooting steps for future reference.

---

