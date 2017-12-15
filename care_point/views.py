from django.shortcuts import render, redirect, get_object_or_404, render_to_response
from datetime import datetime as fdt
import datetime as idt
from .forms import *
import itertools


def index(request):
    info = 'info'
    return render(request, 'care_point/index.html', {'info': info})


#CONTRACT
def contract(request):
    contracts = Contract.objects.all()
    return render(request, 'care_point/contract/contract.html', {'contracts': contracts})


def contract_update(request, contract_id):
    c = get_object_or_404(Contract, pk=contract_id)
    form = ContractForm(data=request.POST or None, instance=c)
    if request.method == 'POST':
        if form.is_valid():
            new = form.save(commit=False)
            new.save()
        return redirect('care_point:contract')
    return render(request, 'care_point/contract/contract_update.html', {'form': form})


def contract_details(request, contract_id):
    contract = get_object_or_404(Contract, pk=contract_id)
    return render(request, 'care_point/contract/contract_details.html', {'contract': contract})


def contract_delete(request, contract_id):
    contract = get_object_or_404(Contract, pk=contract_id)
    contract.delete()
    return redirect('care_point:contract')


def contract_add(request):
    if request.method == 'POST':
        form = ContractForm(data=request.POST)
        if form.is_valid():
            new = form.save(commit=False)
            new.save()
        return redirect('care_point:contract')
    else:
        form = ContractForm()
        return render(request, 'care_point/contract/contract_add.html', {'form': form})


def contract_add_caregiver(request):
    if request.method == 'POST':
        form = ContractForm(data=request.POST)
        if form.is_valid():
            new = form.save(commit=False)
            new.save()
            caregiver.contract_set.add(new)
        return redirect('care_point:caregiver')
    else:
        form = ContractForm()
        return render(request, 'care_point/contract/contract_add.html', {'form': form})


def next_contract(request, caregiver_id):
    if request.method == 'POST':
        form = ContractForm(data=request.POST)
        if form.is_valid():
            new = form.save(commit=False)
            caregiver = get_object_or_404(Caregiver, pk=caregiver_id)
            new.save()
            caregiver.contract_set.add(new)
        return redirect('care_point:caregiver')
    else:
        form = ContractForm()
        return render(request, 'care_point/contract/contract_add.html', {'form': form})


#CAREGIVER
def caregiver(request):
    c = Caregiver.objects.all()
    return render(request, 'care_point/caregiver/caregiver.html', {'caregivers': c})


def caregiver_add(request):
    if request.method == 'POST':
        form_caregiver = CaregiverForm(data=request.POST)
        form_contract = ContractForm(data=request.POST)

        if form_caregiver.is_valid() and form_contract.is_valid():
            caregiver = form_caregiver.save(commit=False)
            check_caregiver = Caregiver.objects.filter(name=caregiver.name).filter(sname=caregiver.sname).first()
            if check_caregiver != None:
                if caregiver.name == check_caregiver.name and caregiver.sname == check_caregiver.sname:
                    info = "Opiekun o tym imieniu i nazwisku znajduje sie w bazie."
                    print(caregiver)
                    form_contract = ContractForm()
                    form_caregiver = CaregiverForm()
                    return render(request, 'care_point/caregiver/caregiver_add.html',
                                  {'form_caregiver': form_caregiver, 'form_contract': form_contract, 'info': info})
            else:
                contract = form_contract.save(commit=False)
                contract.save()
                caregiver.save()
                caregiver.contract_set.add(contract)
        return redirect('care_point:caregiver')
    else:
        form_contract = ContractForm()
        form_caregiver = CaregiverForm()
        return render(request, 'care_point/caregiver/caregiver_add.html',
                      {'form_caregiver': form_caregiver, 'form_contract': form_contract})


def caregiver_details(request, caregiver_id):
    caregiver = get_object_or_404(Caregiver, pk=caregiver_id)
    contract = caregiver.contract_set.all()
    worksheet = list(caregiver.worksheet_set.all())
    iterator = 1
    month_now = idt.datetime.now().month
    url_str = "care_point:worksheet_details"

    calendar = '<div class="col-sm-12 col-md-12"><div class="conteiner-fluid">'
    calendar += '<table id="calendar"><tbody>'
    for i in range(0, 5):
        if iterator % 7 == 1:
            print("pierwszy if: " + iterator.__str__())
            calendar += '<tr class="calendar_tr">'
        for j in range(0, 7):
            for w in worksheet:
                if w.date.month == month_now:
                    if w.date.day == iterator:
                        if iterator % 7 == 1:
                            calendar += '<tr class="calendar_tr">'
                        calendar += '<td class="calendar_td">' + iterator.__str__() + '<br>'
                        for w_for_day in worksheet:
                            if w_for_day.date.day == iterator:
                                calendar += '<a href="' + '/care_point/worksheet/'+ w.id.__str__() + '/'  '"> ' + w.ward.__str__() +'</a><br>'
                        iterator += 1
                        calendar += '</td>'
                        if iterator % 7 == 1:
                            calendar += '</tr>'
            else:
                if iterator < 32:
                    calendar += '<td class="calendar_td">' +iterator.__str__() + '<br></td>'
                    iterator += 1
            if iterator % 7 == 1:
                calendar += '</tr>'

    calendar += '</tbody></table></div></div>'

    return render(request, 'care_point/caregiver/caregiver_details.html',
                  {'caregiver': caregiver, 'contract': contract, 'worksheet': worksheet, 'calendar': calendar})


def caregiver_update(request, caregiver_id):
    c = get_object_or_404(Caregiver, pk=caregiver_id)
    form = CaregiverForm(data=request.POST or None, instance=c)
    if request.method == 'POST':
        if form.is_valid():
            new = form.save(commit=False)
            new.save()
        return redirect('care_point:caregiver')
    return render(request, 'care_point/caregiver/caregiver_update.html', {'form': form})


def caregiver_delete(request, caregiver_id):
    caregiver = get_object_or_404(Caregiver, pk=caregiver_id)
    caregiver.delete()
    return redirect('care_point:caregiver')


def illness(request):
    illness = Illness.objects.all()
    return render(request, 'care_point/illness/illness.html', {'illness': illness})


def illness_add(request):
    if request.method == 'POST':
        form = IllnessForm(data=request.POST)
        if form.is_valid():
            illness = form.save(commit=False)
            illness.save()
        return redirect('care_point:illness')
    else:
        form = IllnessForm()
        return render(request, 'care_point/illness/illness_add.html', {'form': form})


def illness_details(request, illness_id):
    illness = get_object_or_404(Illness, pk=illness_id)
    return render(request, 'care_point/illness/illness_details.html', {'illness': illness})


def illness_update(request, illness_id):
    i = get_object_or_404(Illness, pk=illness_id)
    form = IllnessForm(data=request.POST or None, instance=i)
    if request.method == 'POST':
        if form.is_valid():
            new = form.save(commit=False)
            new.save()
        return redirect('care_point:illness')
    return render(request, 'care_point/illness/illness_update.html', {'form': form})


def illness_delete(request, illness_id):
    illness = get_object_or_404(Illness, pk=illness_id)
    illness.delete()
    return redirect('care_point:illness')


def activity(request):
    activity = Activity.objects.all()
    return render(request, 'care_point/activity/activity.html', {'activity': activity})

# ACTIVITY
def activity_add(request):
    if request.method == 'POST':
        form = ActivityForm(data=request.POST)
        if form.is_valid():
            activity = form.save(commit=False)
            activity.save()
        return redirect('care_point:activity')
    else:
        form = ActivityForm()
        return render(request, 'care_point/activity/activity_add.html', {'form': form})


def activity_details(request, activity_id):
    activity = get_object_or_404(Activity, pk=activity_id)
    return render(request, 'care_point/activity/activity_details.html', {'activity': activity})


def activity_update(request, activity_id):

    a = get_object_or_404(Activity, pk=activity_id)
    form = ActivityForm(data=request.POST or None, instance=a)
    if request.method == 'POST':
        if form.is_valid():
            new = form.save(commit=False)
            new.save()
        return redirect('care_point:activity')
    return render(request, 'care_point/activity/activity_update.html', {'form': form})


def activity_delete(request, activity_id):
    activity = get_object_or_404(Activity, pk=activity_id)
    activity.delete()
    return redirect('care_point:activity')


#WARD
def ward(request):
    ward = Ward.objects.all()
    return render(request, 'care_point/ward/ward.html', {'ward': ward})


def ward_add(request):
    if request.method == 'POST':
        form_ward = WardForm(data=request.POST)
        form_decision = DecisionForm(data=request.POST)
        if form_ward.is_valid() and form_decision.is_valid():
            ward = form_ward.save(commit=False)
            check_ward = Ward.objects.filter(name=ward.name).filter(sname=ward.sname).filter(pesel=ward.pesel).first()

            if check_ward != None:
                if ward.name == check_ward.name and ward.sname == check_ward.sname and ward.pesel == check_ward.pesel:
                    info = "Podopieczny o tym imieniu, nazwisku oraz peselu znajduje sie w bazie."
                    form_ward = WardForm()
                    form_decision = DecisionForm()
                    return render(request, 'care_point/ward/ward_add.html',
                                  {'form_ward': form_ward, 'form_decision': form_decision, 'info': info})
            else:
                decision = form_decision.save(commit=False)
                ward.save()
                decision.save()
                ward.decision_set.add(decision)
        return redirect('care_point:ward')
    else:
        form_ward = WardForm()
        form_decision = DecisionForm()
        return render(request, 'care_point/ward/ward_add.html', {'form_ward': form_ward, 'form_decision': form_decision})

def ward_details(request, ward_id):
    ward = get_object_or_404(Ward, pk=ward_id)
    decision = ward.decision_set.all()
    worksheet = ward.worksheet_set.all()
    return render(request, 'care_point/ward/ward_details.html', {'ward': ward, 'decision': decision, 'worksheet':worksheet })


def ward_update(request, ward_id):

    w = get_object_or_404(Ward, pk=ward_id)
    form = WardForm(data=request.POST or None, instance=w)
    if request.method == 'POST':
        if form.is_valid():
            new = form.save(commit=False)
            new.save()
        return redirect('care_point:ward')
    return render(request, 'care_point/ward/ward_update.html', {'form': form})


def ward_delete(request, ward_id):
    ward = get_object_or_404(Ward, pk=ward_id)
    ward.delete()
    return redirect('care_point:ward')


# ADDRESS
def address(request):
    address = Address.objects.all()
    return render(request, 'care_point/address/address.html', {'address': address})


def address_add(request):
    if request.method == 'POST':
        form = AddressForm(data=request.POST)
        if form.is_valid():
            new = form.save(commit=False)
            new.save()
            # ward_id = new.id
        # return render(request, 'care_point/ward/address_add.html', {'ward_id': ward_id})
        return redirect('care_point:address')
    else:
        form = AddressForm()
        return render(request, 'care_point/address/address_add.html', {'form': form})


def address_details(request, address_id):
    address = get_object_or_404(Address, pk=address_id)
    return render(request, 'care_point/address/address_details.html', {'address': address})


def address_update(request, address_id):

    a = get_object_or_404(Address, pk=address_id)
    form = AddressForm(data=request.POST or None, instance=a)
    if request.method == 'POST':
        if form.is_valid():
            new = form.save(commit=False)
            new.save()
        return redirect('care_point:address')
    return render(request, 'care_point/address/address_update.html', {'form': form})


def address_delete(request, address_id):
    address = get_object_or_404(Address, pk=address_id)
    address.delete()
    return redirect('care_point:address')


# DECISION
def decision(request):
    decision = Decision.objects.all()
    return render(request, 'care_point/decision/decision.html', {'decision': decision})


def decision_add(request):
    if request.method == 'POST':
        form = DecisionForm(data=request.POST)
        if form.is_valid():
            new = form.save(commit=False)
            new.save()
        return redirect('care_point:decision')
    else:
        form = DecisionForm()
        return render(request, 'care_point/decision/decision_add.html', {'form': form})


def decision_details(request, decision_id):
    decision = get_object_or_404(Decision, pk=decision_id)
    return render(request, 'care_point/decision/decision_details.html', {'decision': decision})


def decision_update(request, decision_id):

    d = get_object_or_404(Decision, pk=decision_id)
    form = DecisionForm(data=request.POST or None, instance=d)
    if request.method == 'POST':
        if form.is_valid():
            new = form.save(commit=False)
            new.save()
        return redirect('care_point:decision')
    return render(request, 'care_point/decision/decision_update.html', {'form': form})


def decision_delete(request, decision_id):
    decision = get_object_or_404(Decision, pk=decision_id)
    decision.delete()
    return redirect('care_point:decision')


def next_decision(request, ward_id):
    if request.method == 'POST':
        form = DecisionForm(data=request.POST)
        if form.is_valid():
            new = form.save(commit=False)
            new.save()
        return redirect('care_point:ward')
    else:
        form = DecisionForm()
        return render(request, 'care_point/decision/decision_add.html', {'form': form})


#WORKSHEET
def worksheet(request):
    worksheet = Worksheet.objects.all()
    return render(request, 'care_point/worksheet/worksheet.html', {'worksheet': worksheet})


def worksheet_add(request):
    if request.method == 'POST':
        form = WorksheetForm(data=request.POST)
        if form.is_valid():
            new = form.save(commit=False)

            caregiver_worksheet_at_date = Worksheet.objects.filter(caregiver=new.caregiver).filter(date=new.date)
            ward_worksheet_at_date = Worksheet.objects.filter(ward=new.ward).filter(date=new.date)
            list(caregiver_worksheet_at_date)
            # list(ward_worksheet_at_date)

            new_time_from = idt.datetime.combine(idt.date(1, 1, 1), new.hour_from)
            new_time_to = idt.datetime.combine(idt.date(1, 1, 1), new.hour_to)
            compare_time = idt.timedelta(0, 0, 0)

            # Checking available of cargiver

            # check_available(request, list(caregiver_worksheet_at_date), new, caregiver, form)

            # ZAMKNAC W METODE I UOGOLNIC

            if len(caregiver_worksheet_at_date) > 0:
                is_free = True
                for i in caregiver_worksheet_at_date:
                    i_time_from = idt.datetime.combine(idt.date(1, 1, 1), i.hour_from)
                    i_time_to = idt.datetime.combine(idt.date(1, 1, 1), i.hour_to)

                    if i_time_from - new_time_from < compare_time:

                        if i_time_to - new_time_from > compare_time or i_time_to - new_time_to > compare_time:
                            is_free = False

                    elif i_time_from - new_time_from > compare_time:

                        if i_time_from - new_time_to < compare_time or i_time_to - new_time_to < compare_time:
                            is_free = False

                    elif new_time_from - new_time_to >= compare_time:
                        info = "Godzina rozpoczecia opieki " + new.hour_from.__str__() + " musi byc wczesniejsza niz godzina zakonczenia " + new.hour_to.__str__() + "."
                        form = WorksheetForm()
                        return render(request, 'care_point/worksheet/worksheet_add.html', {'form': form, "info": info})

                    else:
                        is_free = False

                if is_free:
                    new.save()
                    return redirect('care_point:worksheet')
                else:
                    info = "W godzinach " + new.hour_from.__str__() + " - " + new.hour_to.__str__() + " pracownik " + new.caregiver.__str__() + " wykonuje inne obowiazki"
                    form = WorksheetForm()
                    return render(request, 'care_point/worksheet/worksheet_add.html', {'form': form, "info": info})
            else:
                new.save()
                return redirect('care_point:worksheet')
    else:
        form = WorksheetForm()
        return render(request, 'care_point/worksheet/worksheet_add.html', {'form': form})


def worksheet_details(request, worksheet_id):
    worksheet = get_object_or_404(Worksheet, pk=worksheet_id)
    return render(request, 'care_point/worksheet/worksheet_details.html', {'worksheet': worksheet})


def worksheet_update(request, worksheet_id):

    w = get_object_or_404(Worksheet, pk=worksheet_id)
    form = WorksheetForm(data=request.POST or None, instance=w)
    if request.method == 'POST':
        if form.is_valid():
            new = form.save(commit=False)
            new.save()
        return redirect('care_point:worksheet')
    return render(request, 'care_point/worksheet/worksheet_update.html', {'form': form})


def worksheet_delete(request, worksheet_id):
    worksheet = get_object_or_404(Worksheet, pk=worksheet_id)
    worksheet.delete()
    return redirect('care_point:worksheet')


def new_worksheet_caregiver(request, caregiver_id):
    if request.method == 'POST':
        form = WorksheetForm(data=request.POST)
        if form.is_valid():
            new = form.save(commit=False)
            new.save()
            caregiver_id_new = new.caregiver.id
            return redirect('care_point:caregiver')
        # return render(request, 'care_point/caregiver/caregiver_details.html', {'caregiver_id': caregiver_id})
    else:
        form = WorksheetForm()
        return render(request, 'care_point/worksheet/worksheet_add.html', {'form': form})


def new_worksheet_ward(request, ward_id):
    if request.method == 'POST':
        form = WorksheetForm(data=request.POST)
        if form.is_valid():
            new = form.save(commit=False)
            new.save()
        return redirect('care_point:ward')
        # return render(request, 'care_point/caregiver/caregiver_details.html', {'caregiver_id': caregiver_id})
    else:
        form = WorksheetForm()
        return render(request, 'care_point/worksheet/worksheet_add.html', {'form': form})


def check_available(request, worksheets, new_worksheet, person, form):
    new_time_from = idt.datetime.combine(idt.date(1, 1, 1), new_worksheet.hour_from)
    new_time_to = idt.datetime.combine(idt.date(1, 1, 1), new_worksheet.hour_to)
    compare_time = idt.timedelta(0, 0, 0)
    if len(worksheets) > 0:
        is_free = True
        for i in worksheets:
            i_time_from = idt.datetime.combine(idt.date(1, 1, 1), i.hour_from)
            i_time_to = idt.datetime.combine(idt.date(1, 1, 1), i.hour_to)

            if i_time_from - new_time_from < compare_time:

                if i_time_to - new_time_from > compare_time or i_time_to - new_time_to > compare_time:
                    is_free = False

            elif i_time_from - new_time_from > compare_time:

                if i_time_from - new_time_to < compare_time or i_time_to - new_time_to < compare_time:
                    is_free = False

            elif new_time_from - new_time_to >= compare_time:
                info = "Godzina rozpoczecia opieki " + new_worksheet.hour_from.__str__() + " musi byc wczesniejsza niz godzina zakonczenia " + new_worksheet.hour_to.__str__() + "."
                form = WorksheetForm()
                return render(request, 'care_point/worksheet/worksheet_add.html', {'form': form, "info": info})

            else:
                is_free = False

        if is_free:
            new_worksheet.save()
            return redirect('care_point:worksheet')
        else:
            info = "W godzinach " + new_worksheet.hour_from.__str__() + " - " + new_worksheet.hour_to.__str__() + " pracownik " + new_worksheet.caregiver.__str__() + " wykonuje inne obowiazki"
            form = WorksheetForm()
            return render(request, 'care_point/worksheet/worksheet_add.html', {'form': form, "info": info})