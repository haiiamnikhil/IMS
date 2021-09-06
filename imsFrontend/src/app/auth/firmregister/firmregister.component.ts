import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { Router } from '@angular/router';
import { FirmService } from 'src/app/services/firm/firm.service';

@Component({
  selector: 'app-firmregister',
  templateUrl: './firmregister.component.html',
  styleUrls: ['./firmregister.component.css']
})
export class FirmregisterComponent implements OnInit {

  form:FormGroup;
  isBusy:boolean = false;
  message:string;
  changeId:boolean = false;
  firmId:string

  constructor(private firm:FirmService, private router:Router, private formBuilder:FormBuilder) { }

  ngOnInit(){
    this.form = this.formBuilder.group({
      firmname: [null,Validators.required],firm_id:[{value:this.firmId,disabled:true},Validators.required],
      password: [null,Validators.required], confirm_pass: [null,Validators.required], firm_email:[null,[Validators.required,Validators.email]],
      addressline1:[null,Validators.required], addressline2:[null,Validators.required],
      city:[null,Validators.required], zipcode:[null,Validators.required], est_year:[null,Validators.required],
      firm_website: [null,Validators.required], country:[null,Validators.required],
      officephone:[null,Validators.required],mobile:[null,[Validators.required]]
    })
  }

 makeid() {
    var text = "";
    var possible = "0123456789";
    for (var i = 0; i <= 9; i++)
      text += possible.charAt(Math.floor(Math.random() * possible.length));
    return text;
  }
  
  changeFirmId(event:any){
    console.log(event)
    this.changeId = true
  }

  generateID(event:any){
    this.form.get('firm_id').setValue(this.makeid())
  }

  registerFirm(){
    this.isBusy = true
    let firmDetails = {
      firmname:this.form.get('firmname').value, firm_id:this.form.get('firm_id').value, firm_email:this.form.get('firm_email').value,
      password:this.form.get('password').value,est_year:this.form.get('est_year').value,firm_website:this.form.get('firm_website').value, address:this.form.get('addressline1').value + ',' + this.form.get('addressline2').value, 
      city:this.form.get('city').value, zipcode:this.form.get('zipcode').value, country:this.form.get('country').value,
      officephone:this.form.get('officephone').value, mobile:this.form.get('mobile').value
    }

    this.firm.registerFirm(firmDetails).subscribe(response => {
      if (response.success){
        this.router.navigate(['/auth/signin/'])
      } else {
        console.log(false)
      }
    }, err => console.log(err))
  }

}
