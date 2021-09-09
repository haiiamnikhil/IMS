import { Injectable } from '@angular/core';
import { Observable } from 'rxjs'
import { HttpClient, HttpHeaders } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class UserService {
  header = new HttpHeaders({'content-type': 'application/json'})
  constructor(private http: HttpClient) { }

  userSignUp(credentials:any): Observable<any>{
    return this.http.post('/signup/user/', credentials)
  }
}
