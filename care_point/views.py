from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404, render_to_response
from datetime import datetime as fdt
import datetime as idt
from .forms import *
import itertools


def index(request):
    info = 'info'
    return render(request, 'care_point/index.html', {'info': info})


#CONTRACT
@login_required
def contract(request):
    contracts = Contract.objects.all()
    return render(request, 'care_point/contract/contract.html', {'contracts': contracts})


@login_required
def contract_update(request, contract_id):
    c = get_object_or_404(Contract, pk=contract_id)
    form = ContractForm(data=request.POST or None, instance=c)
    if request.method == 'POST':
        if form.is_valid():
            new = form.save(commit=False)
            new.save()
        return redirect('care_point:contract')
    return render(request, 'care_point/contract/contract_update.html', {'form': form})


@login_required
def contract_details(request, contract_id):
    contract = get_object_or_404(Contract, pk=contract_id)
    return render(request, 'care_point/contract/contract_details.html', {'contract': contract})


@login_required
def contract_delete(request, contract_id):
    contract = get_object_or_404(Contract, pk=contract_id)
    contract.delete()
    return redirect('care_point:contract')


@login_required
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


@login_required
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


@login_required
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
@login_required
def caregiver(request):
    c = Caregiver.objects.all()
    return render(request, 'care_point/caregiver/caregiver.html', {'caregivers': c})


@login_required
def caregiver_add(request):
    if request.method == 'POST':
        form_caregiver = CaregiverForm(data=request.POST)

        # form_contract.clean_data['data']  : dostep do pola formularza

        form_contract = ContractForm(data=request.POST)

        if form_caregiver.is_valid() and form_contract.is_valid():
            caregiver = form_caregiver.save(commit=False)
            check_caregiver = Caregiver.objects.filter(name=caregiver.name).filter(sname=caregiver.sname).first()
            if check_caregiver != None:
                if caregiver.name == check_caregiver.name and caregiver.sname == check_caregiver.sname:
                    info = "Opiekun o tym imieniu i nazwisku znajduje sie w bazie."
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
        # dodawanie wartosci do formularza
        # from = searchTeeamForm({'name': " fc b "})
        return render(request, 'care_point/caregiver/caregiver_add.html',
                      {'form_caregiver': form_caregiver, 'form_contract': form_contract})


@login_required
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
                                calendar += '<a href="' + '/care_point/worksheet/'+ w_for_day.id.__str__() + '/'  '"> ' + w_for_day.ward.__str__() +'</a><br>'
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


@login_required
def caregiver_update(request, caregiver_id):
    c = get_object_or_404(Caregiver, pk=caregiver_id)
    form = CaregiverForm(data=request.POST or None, instance=c)
    if request.method == 'POST':
        if form.is_valid():
            new = form.save(commit=False)
            new.save()
        return redirect('care_point:caregiver')
    return render(request, 'care_point/caregiver/caregiver_update.html', {'form': form})


@login_required
def caregiver_delete(request, caregiver_id):
    caregiver = get_object_or_404(Caregiver, pk=caregiver_id)
    caregiver.delete()
    return redirect('care_point:caregiver')


@login_required
def illness(request):
    illness = Illness.objects.all()
    return render(request, 'care_point/illness/illness.html', {'illness': illness})


@login_required
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


@login_required
def illness_details(request, illness_id):
    illness = get_object_or_404(Illness, pk=illness_id)
    return render(request, 'care_point/illness/illness_details.html', {'illness': illness})


@login_required
def illness_update(request, illness_id):
    i = get_object_or_404(Illness, pk=illness_id)
    form = IllnessForm(data=request.POST or None, instance=i)
    if request.method == 'POST':
        if form.is_valid():
            new = form.save(commit=False)
            new.save()
        return redirect('care_point:illness')
    return render(request, 'care_point/illness/illness_update.html', {'form': form})


@login_required
def illness_delete(request, illness_id):
    illness = get_object_or_404(Illness, pk=illness_id)
    illness.delete()
    return redirect('care_point:illness')


@login_required
def activity(request):
    activity = Activity.objects.all()
    return render(request, 'care_point/activity/activity.html', {'activity': activity})


# ACTIVITY
@login_required
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


@login_required
def activity_details(request, activity_id):
    activity = get_object_or_404(Activity, pk=activity_id)
    return render(request, 'care_point/activity/activity_details.html', {'activity': activity})


@login_required
def activity_update(request, activity_id):

    a = get_object_or_404(Activity, pk=activity_id)
    form = ActivityForm(data=request.POST or None, instance=a)
    if request.method == 'POST':
        if form.is_valid():
            new = form.save(commit=False)
            new.save()
        return redirect('care_point:activity')
    return render(request, 'care_point/activity/activity_update.html', {'form': form})


@login_required
def activity_delete(request, activity_id):
    activity = get_object_or_404(Activity, pk=activity_id)
    activity.delete()
    return redirect('care_point:activity')


#WARD
@login_required
def ward(request):
    ward = Ward.objects.all()
    return render(request, 'care_point/ward/ward.html', {'ward': ward})


@login_required
def ward_add(request):
    if request.method == 'POST':
        form_ward = WardForm(data=request.POST)
        form_decision = DecisionForm(data=request.POST)
        form_address = AddressForm(data=request.POST)
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
                address = form_address.save(commit=False)
                ward.save()
                decision.save()
                address.save()
                ward.decision_set.add(decision)
                ward.address_set.add(address)
                ill = form_decision.cleaned_data['illness']
                act = form_decision.cleaned_data['activity']
                for i in ill:
                    decision.illness.add(i)
                for a in act:
                    decision.activity.add(a)
        return redirect('care_point:ward')
    else:
        form_ward = WardForm()
        form_decision = DecisionForm()
        form_address = AddressForm()
        return render(request, 'care_point/ward/ward_add.html', {'form_ward': form_ward, 'form_decision': form_decision, 'form_address': form_address})


@login_required
def ward_details(request, ward_id):
    ward = get_object_or_404(Ward, pk=ward_id)
    decision = ward.decision_set.all()
    worksheet = ward.worksheet_set.all()
    return render(request, 'care_point/ward/ward_details.html', {'ward': ward, 'decision': decision, 'worksheet':worksheet })


@login_required
def ward_update(request, ward_id):

    w = get_object_or_404(Ward, pk=ward_id)
    form = WardForm(data=request.POST or None, instance=w)
    if request.method == 'POST':
        if form.is_valid():
            new = form.save(commit=False)
            new.save()
        return redirect('care_point:ward')
    return render(request, 'care_point/ward/ward_update.html', {'form': form})


@login_required
def ward_delete(request, ward_id):
    ward = get_object_or_404(Ward, pk=ward_id)
    ward.delete()
    return redirect('care_point:ward')


# ADDRESS
@login_required
def address(request):
    address = Address.objects.all()
    return render(request, 'care_point/address/address.html', {'address': address})


@login_required
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


@login_required
def address_details(request, address_id):
    address = get_object_or_404(Address, pk=address_id)
    return render(request, 'care_point/address/address_details.html', {'address': address})


@login_required
def address_update(request, address_id):

    a = get_object_or_404(Address, pk=address_id)
    form = AddressForm(data=request.POST or None, instance=a)
    if request.method == 'POST':
        if form.is_valid():
            new = form.save(commit=False)
            new.save()
        return redirect('care_point:address')
    return render(request, 'care_point/address/address_update.html', {'form': form})


@login_required
def address_delete(request, address_id):
    address = get_object_or_404(Address, pk=address_id)
    address.delete()
    return redirect('care_point:address')


# DECISION
@login_required
def decision(request):
    decision = Decision.objects.all()
    return render(request, 'care_point/decision/decision.html', {'decision': decision})


@login_required
def decision_add(request):
    if request.method == 'POST':
        form = DecisionForm(data=request.POST)
        if form.is_valid():
            new = form.save(commit=False)
            new.save()
            ill = form.cleaned_data['illness']
            act = form.cleaned_data['activity']
            for i in ill:
                new.illness.add(i)
            for a in act:
                new.activity.add(a)
        return redirect('care_point:decision')
    else:
        form = DecisionForm()
        return render(request, 'care_point/decision/decision_add.html', {'form': form})


@login_required
def decision_details(request, decision_id):
    decision = get_object_or_404(Decision, pk=decision_id)
    return render(request, 'care_point/decision/decision_details.html', {'decision': decision})


@login_required
def decision_update(request, decision_id):

    d = get_object_or_404(Decision, pk=decision_id)
    form = DecisionForm(data=request.POST or None, instance=d)
    if request.method == 'POST':
        if form.is_valid():
            new = form.save(commit=False)
            new.save()
        return redirect('care_point:decision')
    return render(request, 'care_point/decision/decision_update.html', {'form': form})


@login_required
def decision_delete(request, decision_id):
    decision = get_object_or_404(Decision, pk=decision_id)
    decision.delete()
    return redirect('care_point:decision')


@login_required
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
@login_required
def worksheet(request):
    worksheet = Worksheet.objects.all()
    return render(request, 'care_point/worksheet/worksheet.html', {'worksheet': worksheet})


@login_required
def worksheet_add(request):
    if request.method == 'POST':
        form = WorksheetForm(data=request.POST)
        if form.is_valid():
            new = form.save(commit=False)

            caregiver_worksheet_at_date = Worksheet.objects.filter(caregiver=new.caregiver).filter(date=new.date)
            ward_worksheet_at_date = Worksheet.objects.filter(ward=new.ward).filter(date=new.date)

            check_caregiver = check_available(caregiver_worksheet_at_date, new)
            check_ward = check_available(ward_worksheet_at_date, new)

            # list(caregiver_worksheet_at_date)
            # list(ward_worksheet_at_date)

            # new_time_from = idt.datetime.combine(idt.date(1, 1, 1), new.hour_from)
            # new_time_to = idt.datetime.combine(idt.date(1, 1, 1), new.hour_to)
            # compare_time = idt.timedelta(0, 0, 0)

            # Checking available of cargiver

            # check_available(request, list(caregiver_worksheet_at_date), new, caregiver, form)

            # ZAMKNAC W METODE I UOGOLNIC

            # if len(caregiver_worksheet_at_date) > 0:
            #     is_free = True
            #     for i in caregiver_worksheet_at_date:
            #         i_time_from = idt.datetime.combine(idt.date(1, 1, 1), i.hour_from)
            #         i_time_to = idt.datetime.combine(idt.date(1, 1, 1), i.hour_to)
            #
            #         if i_time_from - new_time_from < compare_time:
            #
            #             if i_time_to - new_time_from > compare_time or i_time_to - new_time_to > compare_time:
            #                 is_free = False
            #
            #         elif i_time_from - new_time_from > compare_time:
            #
            #             if i_time_from - new_time_to < compare_time or i_time_to - new_time_to < compare_time:
            #                 is_free = False
            #
            #         elif new_time_from - new_time_to >= compare_time:
            #             info = "Godzina rozpoczecia opieki " + new.hour_from.__str__() + " musi byc wczesniejsza niz godzina zakonczenia " + new.hour_to.__str__() + "."
            #             form = WorksheetForm()
            #             return render(request, 'care_point/worksheet/worksheet_add.html', {'form': form, "info": info})
            #
            #         else:
            #             is_free = False

            if check_caregiver and check_ward:
                new.save()
                return redirect('care_point:worksheet')
            elif not check_caregiver:
                info = "W godzinach " + new.hour_from.__str__() + " - " + new.hour_to.__str__() + " pracownik " + new.caregiver.__str__() + " wykonuje inne obowiazki"
                form = worksheet_form_with_content(new)
                return render(request, 'care_point/worksheet/worksheet_add.html', {'form': form, "info": info})
            elif not check_ward:
                info = "W godzinach " + new.hour_from.__str__() + " - " + new.hour_to.__str__() + " podopieczny " + new.ward.__str__() + " ma inna wizyte"
                form = worksheet_form_with_content(new)
                return render(request, 'care_point/worksheet/worksheet_add.html', {'form': form, "info": info})
            # else:
            #     new.save()
            #     return redirect('care_point:worksheet')
    else:
        form = WorksheetForm()
        return render(request, 'care_point/worksheet/worksheet_add.html', {'form': form})


@login_required
def worksheet_details(request, worksheet_id):
    worksheet = get_object_or_404(Worksheet, pk=worksheet_id)

    ward = Ward.objects.filter(pk=worksheet.ward_id).first()
    address = list(Address.objects.filter(ward=ward).all())
    ward_decisions =ward.decision_set.all()

    ward_activity = []
    ward_illness = []
    for decision in ward_decisions:
        wl = list(decision.illness.all())
        wa = list(decision.activity.all())
        ward_illness = set(ward_illness + wl)
        ward_activity = set(ward_activity + wa)
        ward_illness = list(ward_illness)
        ward_activity = list(ward_activity)
    return render(request, 'care_point/worksheet/worksheet_details.html', {'worksheet': worksheet, 'ward_illness': ward_illness, 'ward_activity': ward_activity, 'address': address})


@login_required
def worksheet_update(request, worksheet_id):

    w = get_object_or_404(Worksheet, pk=worksheet_id)
    form = WorksheetForm(data=request.POST or None, instance=w)
    if request.method == 'POST':
        if form.is_valid():
            new = form.save(commit=False)
            new.save()
        return redirect('care_point:worksheet')
    return render(request, 'care_point/worksheet/worksheet_update.html', {'form': form})


@login_required
def worksheet_delete(request, worksheet_id):
    worksheet = get_object_or_404(Worksheet, pk=worksheet_id)
    worksheet.delete()
    return redirect('care_point:worksheet')


@login_required
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


@login_required
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


def check_available(worksheets, new_worksheet):
    new_time_from = idt.datetime.combine(idt.date(1, 1, 1), new_worksheet.hour_from)
    new_time_to = idt.datetime.combine(idt.date(1, 1, 1), new_worksheet.hour_to)
    compare_time = idt.timedelta(0, 0, 0)
    is_free = True
    if len(worksheets) > 0:
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
                is_free = False

            else:
                is_free = False

    return is_free


def worksheet_form_with_content(data):
    form = WorksheetForm({
        'caregiver': data.caregiver,
        'ward': data.ward,
        'decision': data.decision,
        'genre': data.genre,
        'date': data.date,
        'hour_from': data.hour_from,
        'hour_to': data.hour_to,
        'description': data.description})
    return form

