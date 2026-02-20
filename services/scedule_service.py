def schedule_class(R_number, start, end, case, course):
    return f"✅ {course} class scheduled in room {R_number} from {start} to {end}. Reason: {case}"

def cancel_class(R_number, time, reason):
    return f"❌ Class in room {R_number} at {time} canceled. Reason: {reason}"

def show_schedule(date):
    return f"📅 Weekly schedule for {date} loaded."
