import frappe


@frappe.whitelist()
def get_patient_details(patient_id=None)
	return frappe.db.sql(f"""SELECT first_name FROM 'tabPatient' WHERE owner='Administrator'""")
