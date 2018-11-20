; ModuleID = 'llvm_tmp.opt1.ll'
target datalayout = "e-m:o-i64:64-f80:128-n8:16:32:64-S128"
target triple = "x86_64-apple-macosx10.14.0"

; Function Attrs: norecurse nounwind readnone ssp uwtable
define void @write_pipe(i8 signext %ch00, i32* nocapture %data0) #0 {
  ret void
}

; Function Attrs: norecurse nounwind readnone ssp uwtable
define void @read_pipe(i8 signext %ch00, i32* nocapture %dataInt0) #0 {
  ret void
}

; Function Attrs: norecurse nounwind readnone ssp uwtable
define i32 @get_pipe_num_packets(i32 %a) #0 {
  ret i32 %a
}

; Function Attrs: norecurse nounwind readnone ssp uwtable
define void @kernelInput(i32* noalias nocapture %aIn0, i32* noalias nocapture %aIn1, i32 %ch00, i32 %ch01) #0 { ret void }

; Function Attrs: norecurse nounwind readnone ssp uwtable
define void @kernelCompute(i32 %ch00, i32 %ch01, i32 %ch1) #0 { ret void }

; Function Attrs: norecurse nounwind ssp uwtable
define void @kernelOutput(i32* noalias nocapture %aOut, i32 %ch1) #1 { 
  %1 = tail call i32 @get_pipe_num_packets(i32 %ch1)
  %2 = icmp eq i32 %1, 0
  br label %.preheader

.preheader:                                       ; preds = %0, %.split
  %i.01 = phi i32 [ 0, %0 ], [ %3, %.split ]
  br i1 %2, label %.preheader.split, label %.split

.preheader.split:                                 ; preds = %.preheader, %.preheader.split
  br label %.preheader.split

.split:                                           ; preds = %.preheader
  %3 = add nuw nsw i32 %i.01, 1
  %4 = icmp slt i32 %3, 10
  br i1 %4, label %.preheader, label %5

; <label>:5                                       ; preds = %.split
  ret void
}

attributes #0 = { norecurse nounwind readnone ssp uwtable "disable-tail-calls"="false" "less-precise-fpmad"="false" "no-frame-pointer-elim"="true" "no-frame-pointer-elim-non-leaf" "no-infs-fp-math"="false" "no-nans-fp-math"="false" "stack-protector-buffer-size"="8" "target-cpu"="core2" "target-features"="+cx16,+fxsr,+mmx,+sse,+sse2,+sse3,+ssse3" "unsafe-fp-math"="false" "use-soft-float"="false" }
attributes #1 = { norecurse nounwind ssp uwtable "disable-tail-calls"="false" "less-precise-fpmad"="false" "no-frame-pointer-elim"="true" "no-frame-pointer-elim-non-leaf" "no-infs-fp-math"="false" "no-nans-fp-math"="false" "stack-protector-buffer-size"="8" "target-cpu"="core2" "target-features"="+cx16,+fxsr,+mmx,+sse,+sse2,+sse3,+ssse3" "unsafe-fp-math"="false" "use-soft-float"="false" }

!llvm.module.flags = !{!0}
!llvm.ident = !{!1}

!0 = !{i32 1, !"PIC Level", i32 2}
!1 = !{!"clang version 3.8.0 (tags/RELEASE_380/final)"}
