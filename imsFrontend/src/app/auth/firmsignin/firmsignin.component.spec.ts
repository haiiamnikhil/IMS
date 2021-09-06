import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { FirmsigninComponent } from './firmsignin.component';

describe('FirmsigninComponent', () => {
  let component: FirmsigninComponent;
  let fixture: ComponentFixture<FirmsigninComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ FirmsigninComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(FirmsigninComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
