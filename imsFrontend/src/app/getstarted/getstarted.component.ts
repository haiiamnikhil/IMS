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
  basicDetails:any = []
  userType:string
  designations = []
  default = "Select"

  constructor(private profile:CommonService,private formBuilder:FormBuilder, private router:Router) { }

  ngOnInit(){
    this.form = this.formBuilder.group({
      firmname:[{value:null,disabled:true},Validators.required],
      user_firmname:[{value:null,disabled:true},Validators.required],
      nnid:[{value:null,disabled:true},Validators.required],
      designation:[this.default,Validators.required],
      fullname:[{value:null,disabled:true},Validators.required],
      email:[{value:null,disabled:true},Validators.required],
      address:[null,Validators.required],city: [null, Validators.required],
      country:[null, Validators.required],zipcode: [null, Validators.required],
      officephone: [null, Validators.required],mobile: [null, Validators.required],
      est_year: [null,Validators.required],website: [null, Validators.required],
    })

    this.profile.onBoardDetails().subscribe(response => {
      if(response.success){
        console.log(response.data)
        this.userDetails = response.data
        this.userType = response.user_type
        this.designations = response.designation
        console.log(this.designations)
        this.populateData(this.userType)
      } else {
        console.log('error')
      }
    }, err => console.log(err))
  }
  populateData(user_type:any) {
    if (user_type == 'firm'){
      this.form.get('firmname').setValue(this.userDetails.firmname)
      this.form.get('email').setValue(this.userDetails.email)
      this.form.get('nnid').setValue(this.userDetails.nnid)
    } else if (user_type == 'firm_user'){
      this.form.get('user_firmname').setValue(this.userDetails.firmname)
      this.form.get('email').setValue(this.userDetails.email)
      this.form.get('fullname').setValue(this.userDetails.fullname)
    }
  }

  saveBasicDetails(){
    this.isBusy = true
    if (this.userType == 'firm'){
      this.basicDetails.push({
        website:this.form.get('website').value,
        address: this.form.get('address').value,
        city: this.form.get('city').value,
        country: this.form.get('country').value,
        zipcode: this.form.get('zipcode').value,
        officephone: this.form.get('officephone').value,
        mobile: this.form.get('mobile').value,
        est_year: this.form.get('est_year').value,
      })
    } else if (this.userType == 'firm_user'){
      this.basicDetails.push({
        designation:this.form.get('designation').value,
        address: this.form.get('address').value,
        city: this.form.get('city').value,
        country: this.form.get('country').value,
        zipcode: this.form.get('zipcode').value,
        mobile: this.form.get('mobile').value,
      })
    }
    console.log(this.basicDetails)
    // this.profile.saveDetails(this.basicDetails).subscribe(response => {
    //   if (response.success){
    //     this.router.navigate(['/home'])
    //   } else {
    //     console.log("Some Error Occured")
    //   }
    // }, err => console.log(err))
  }
}
