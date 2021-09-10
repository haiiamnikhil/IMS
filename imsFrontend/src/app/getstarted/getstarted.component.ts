import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { Router } from '@angular/router';
import { CommonService } from '../services/common/common.service';

@Component({
  selector: 'app-getstarted',
  templateUrl: './getstarted.component.html',
  styleUrls: ['./getstarted.component.css']
})
export class GetstartedComponent implements OnInit {
  
  userDetails:any
  form:FormGroup;
  isBusy:boolean = false;

  constructor(private profile:CommonService,private formBuilder:FormBuilder, private router:Router) { }

  ngOnInit(){
    this.form = this.formBuilder.group({
      firmname:[{value:null,disabled:true},Validators.required],
      nnid:[{value:null,disabled:true},Validators.required],
      email:[{value:null,disabled:true},Validators.required],
      address:[null,Validators.required],city: [null, Validators.required],
      country:[null, Validators.required],zipcode: [null, Validators.required],
      officephone: [null, Validators.required],mobile: [null, Validators.required],
      est_year: [null,Validators.required],website: [null, Validators.required],
    })

    this.profile.onBoardDetails().subscribe(response => {
      if(response.success){
        this.userDetails = response.data
        this.populateData()
      } else {
        console.log('error')
      }
    }, err => console.log(err))
  }
  populateData(){
    this.form.get('firmname').setValue(this.userDetails.firmname)
    this.form.get('email').setValue(this.userDetails.email)
    this.form.get('nnid').setValue(this.userDetails.nnid)
  }

  saveBasicDetails(){
    this.isBusy = true
    console.log(this.form.getRawValue())
    let basicDetails = {
      firmname: this.userDetails.firmname,
      email: this.userDetails.email,
      nnid: this.userDetails.nnid,
      website:this.form.get('website').value,
      address: this.form.get('address').value,
      city: this.form.get('city').value,
      country: this.form.get('country').value,
      zipcode: this.form.get('zipcode').value,
      officephone: this.form.get('officephone').value,
      mobile: this.form.get('mobile').value,
      est_year: this.form.get('est_year').value,
    }
    this.profile.saveBasicDetails(basicDetails).subscribe(response => {
      if (response.success){
        this.router.navigate(['/home'])
      } else {
        console.log("Some Error Occured")
      }
    }, err => console.log(err))
  }
}
