# add package
    - uv add [package]

# https://dev.to/tylerlwsmith/defining-tasks-brokers-workers-and-backends-in-celery-1982
# https://derlin.github.io/introduction-to-fastapi-and-celery/03-celery/

# Note
    - Don't forget to restart the worker, as the method definition changed! 

# default command
    - celery -A django_uv worker --loglevel=info
    ✅ Easier to manage
    ✅ Processes all types of tasks
    ❌ No task prioritization
    ❌ A single worker could be overloaded with long-running tasks

# Queue Commands
    - celery -A django_uv worker --loglevel=info --queues=short_tasks
    - celery -A django_uv worker --loglevel=info --queues=long_tasks
    - celery -A django_uv worker --loglevel=info --queues=system_tasks
    ✅ More control over task execution
    ✅ Prevents long-running tasks from blocking short ones
    ✅ Allows scaling workers based on task load
    ❌ More setup and resource usage

# How Celery Handles Queues Without --queues
    - By default, a Celery worker listens to all queues if no specific queue is mentioned.
    - The worker will pull tasks from any queue as they become available.
    
# When Should You Run Multiple Workers (with --queues)?
Running separate workers for different queues is useful when:

    - You want to allocate different resources for different types of tasks.
        Example: Long tasks might need high-memory workers, while short tasks need fast CPU workers.
    - You want to prioritize certain types of tasks.
        Example: A dedicated worker for short_tasks will process quick tasks without waiting for long tasks to complete.
    - You want task isolation to prevent one type of task from blocking another.
        Example: If long-running tasks pile up, they won't delay system-critical tasks.
