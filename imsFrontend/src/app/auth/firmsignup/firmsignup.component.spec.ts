import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { FirmSignupComponent } from './firmsignup.component';

describe('FirmSignupComponent', () => {
  let component: FirmSignupComponent;
  let fixture: ComponentFixture<FirmSignupComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ FirmSignupComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(FirmSignupComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
