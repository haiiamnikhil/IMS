import { Injectable } from '@angular/core';
import { Observable } from 'rxjs'
import {HttpClient, HttpHeaders} from '@angular/common/http'

@Injectable({
  providedIn: 'root'
})
export class FirmService {
  header = new HttpHeaders({'Content-Type': 'application/json'})
  
  constructor(private http: HttpClient) { }

  registerFirm(firmDetails:any): Observable<any>{
    return this.http.post('/firm/register-firm/', firmDetails)
  }

  signInFirm(credentials:any): Observable<any>{
    return this.http.post('/auth/signin/firm/', credentials)
  }
}
