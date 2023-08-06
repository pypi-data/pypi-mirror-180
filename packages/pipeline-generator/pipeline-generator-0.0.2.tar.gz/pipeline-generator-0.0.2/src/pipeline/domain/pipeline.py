import traceback, time
from typing import List, Tuple, Dict, Optional, Callable
from ddd_objects.domain.exception import OperationError
from .value_obj import (
    PipelineOutput,
    PipelineIndicator,
    PipelineContext,
    Name
)
from .value_obj import Name
from .entity import PipelineActionOutput, PipelineStage



class CyclePipelineTemplate:
    def __init__(
        self, 
        stages:List[PipelineStage], 
        context: PipelineContext,
        output_fn: Optional[Callable]=None,
    ) -> None:
        self.stages = stages
        self.__stage_idx_map = {s.stage_name:i for i,s in enumerate(stages)}
        self.__curr_stage_idx = -1
        self.__stage_num = len(stages)
        self.__output_fn = output_fn
        self.context = context
        self.indicator = PipelineIndicator()
        self.status = {}
    

    def __next_stage(self)->Tuple[str, Callable, bool]:
        self.__curr_stage_idx = (self.__curr_stage_idx+1)%self.__stage_num
        stage = self.stages[self.__curr_stage_idx]
        return stage.stage_name, stage.action, stage.allow_failure
    

    def __jump_to(self, stage:Name):
        stage_idx = self.__stage_idx_map[stage.get_value()]
        self.__curr_stage_idx = (stage_idx-1)%self.__stage_num


    def run(self):
        indicator = self.indicator
        if indicator.is_wait() or indicator.is_over():
            pass

        elif indicator.is_pass():
            stage, func, allow_failure = self.__next_stage()
            self.status = {
                'stage': stage,
                'action': func,
                'context': self.context,
                'indictor': self.indicator,
                'allow_failure': allow_failure
            }

        elif indicator.is_run() or indicator.is_run_again():
            if indicator.is_run():
                stage, func, allow_failure = self.__next_stage()
                self.status['stage'] = stage
                self.status['action'] = func
                self.status['allow_failure'] = allow_failure
            else:
                func = self.status['action']
                allow_failure = self.status['allow_failure']
                stage = self.status['stage']
            try:
                output:PipelineActionOutput = func(self.context)
                self.context = output.context
                self.indicator = output.indicator
                self.output = output.output
                jump_stage = output.jump_stage
                if jump_stage is not None:
                    self.__jump_to(jump_stage)
                self.status = {
                    'stage': stage,
                    'action': func,
                    'context': self.context,
                    'indictor': self.indicator,
                    'allow_failure': allow_failure,
                    'output': self.output
                }
            except:
                if not allow_failure:
                    raise OperationError(traceback.format_exc())
                else:
                    self.indicator.set_run_again()
        return self.status

    def is_over(self):
        return self.indicator.is_over()

    def get_output(self, x=None):
        if self.__output_fn is None:
            return self.output
        else:
            return self.__output_fn(self.output, x)

    def run_until_complete(self, timeout=100, interval=1):
        x = []
        for i in range(timeout):
            status = self.run()
            if self.output:
                x.append(self.output)
            if self.is_over():
                return self.get_output(x)
            time.sleep(interval)
        raise OperationError(f'Timeout ({timeout}s) when running loop')



class PipelineGenerator:

    def generate_pipeline(self):
        raise NotImplementedError

    def set_output(self, output: Optional[PipelineOutput]):
        raise NotImplementedError

    def _set_run_again_output(self, context):
        return PipelineActionOutput(
            PipelineContext(context),
            PipelineIndicator().set_run_again()
        )
    def _set_run_next_output(self, context):
        return PipelineActionOutput(PipelineContext(context))

    def _set_over_output(self, context, output=None):
        return PipelineActionOutput(
            PipelineContext(context),
            PipelineIndicator().set_over(),
            output=output
        )

    def _set_jump_output(self, context, action_name):
        return PipelineActionOutput(
            PipelineContext(context),
            PipelineIndicator(),
            Name(action_name)
        )
